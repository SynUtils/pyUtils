
import requests
import json
import time
import datetime
import csv
from dateutil import parser
from jira.client import JIRA
import datetime
import os

"""
Deps:
sudo pip install python-dateutil --force-reinstall
sudo pip install jira
"""




def authenticate_and_addComment_in_jira(issue_id, comment):
	"""
	Authenticate jira  and adding comment in jira
	issue
	"""
	jira_url = 'https://issues.quickoffice.com'
	user_name = 'developer.synerzip'
	password = 'Dev#@!45R'
	
	# Set up JIRA server URL
	jira_options = {
	'server': jira_url
	}

	#Connect to JIRA server using above URL and authentication details
	jira=JIRA(options=jira_options,basic_auth=(user_name,password))
	projects = jira.projects()
	issue = jira.issue(issue_id)
	print issue
	print comment
	jira.add_comment(issue, comment)


def gerrit_req(url):
	"""
	Request to gerrit 
	and return the specific changes

	"""
	return requests.get(url)

def getJSON_Data(changes):
	"""
	To get JSON data from changes that we requested to gerrit

	"""
	changeText = changes.text.split(']}\'')
	return json.loads(changeText[1])


def getGerritData(url, lastUpdate_change_id, output_file ):
	"""
	Getting all details as
		1. Changes merged into master as per date we specified
		2. Commit message for each changeset
		3. Commit id, author_name, author_id

	"""
	changes = gerrit_req(url)
	json_data = getJSON_Data(changes)
	#print json_data

	with open(output_file,'w') as _file:
		_file.write(json_data[0].get('change_id'))

	for chainSet in json_data:
		print chainSet.get('change_id')
		print "Last Updated :", lastUpdate_change_id
		if (chainSet.get('change_id') == lastUpdate_change_id):
			return
		dataUrl = 'https://quickoffice-internal-review.googlesource.com/a/changes/' + chainSet.get('change_id') +\
		'/detail/&format=JSON?o=CURRENT_REVISION&o=CURRENT_COMMIT'

		changes = gerrit_req(dataUrl)
		if changes:
			detailChangeJson = getJSON_Data(changes)

			# Getting commit message for each changeset
			commit_message = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('message')

			#Getting url for each changeset 
			url = 'https://quickoffice-internal.googlesource.com/html-office/+/' + str(detailChangeJson.get('current_revision'))

			#Getting author for each changeset
			author_name = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('author').get('name')
			#Getting author email_id for each changeset
			author_id = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('author').get('email')

			#Building commit message for to write in jira issue
			comment = 'A CL relevant for this Jira is merged with master:' + '\n' + 'Revision: ' + url + '\n' +\
			 'commit: ' + str(detailChangeJson.get('current_revision')) + '\n' +\
			 'Author: ' + author_name + ' <' + author_id + '>' + '\n' +\
			 'Date: ' + parser.parse(chainSet.get('updated')).strftime("%a %b %d %H:%M:%S %Y") + ' +0000'
		
			for index,line in enumerate(str(commit_message).splitlines()):
				if 'BUG' in line:
					bugs = str(commit_message).splitlines()[index:]
					for bug in bugs:
						if not bug.rfind('/') == -1:
							issue_id = bug[bug.rfind('/')+1:]
							if issue_id.endswith(','):
								issue_id = issue_id[:issue_id.rfind(',')]
							#print comment
							authenticate_and_addComment_in_jira(issue_id, comment)
						if not bug.endswith(',') == 1:
							break				    

if __name__ == '__main__':
	# Url for having change status as merged into master
	# print os.getcwd()
	master_url = 'https://quickoffice-internal-review.googlesource.com/a/changes/?q=status:merged+project:html-office+branch:master'
	last_update_change_id = 'If533ef74caef5fe251f47b2390ad6c851cde8dc9'

	input_file = os.path.join(os.getcwd(), "last_updated_changed_id.txt")
	with open(input_file) as _file:
		last_update_change_id = _file.readline()
	getGerritData(master_url,last_update_change_id, input_file)
