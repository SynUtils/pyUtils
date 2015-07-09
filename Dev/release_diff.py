import requests
import json
import csv
from dateutil import parser
from bs4 import BeautifulSoup
import urllib2
import argparse
from jira.client import JIRA
import csv

csv_handler = open( "report.csv", "wb" )
csv_writer = csv.writer(csv_handler)
csv_writer.writerow(["Build URL", "Change Id", "Jira URL", "Jira Summary"])

def write_to_csv(change_id, issue_url, jira_summary):
    # open csv file
    csv_handler = open( "report.csv", "wb" )
    csv_writer = csv.writer(csv_handler)
    csv_writer.writerow([change_id, issue_url, jira_summary])

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
    if len(changeText) == 2:
        return json.loads(changeText[1])
    else:
        return "Error"

def getEntire_Data():   
    url = 'https://quickoffice-internal-review.googlesource.com/a/changes/?q=status:merged+project:html-office+branch:master'
    changes = gerrit_req(url)
    json_data = getJSON_Data(changes)
    return json_data    


def authenticateJira_and_getSummary(issue_id):
    """
    Authenticate jira  and adding comment in jira
    issue
    """

    #cafile = '/Users/nagmani/Documents/public.crt'
    # Set up JIRA server URL
    jira_options = {
    'server': 'https://issues.quickoffice.com'
    }

    #Connect to JIRA server using above URL and authentication details
    jira=JIRA(options=jira_options,basic_auth=('developer.synerzip','Dev#@!45R'))
    projects = jira.projects()
    try:
        issue = jira.issue(issue_id)
        print "summary: ", issue.fields.summary
        print "resolution: ", issue.fields
        return issue.fields.summary
    except Exception, e:
        return "NotValid"

def process_data(change_id, json_data, actual_url):
    # Url for having change status as merged into maste
    for chainSet in json_data:
        change_id = change_id.strip()
        dataUrl = 'https://quickoffice-internal-review.googlesource.com/a/changes/' + change_id +\
        '/detail/&format=JSON?o=CURRENT_REVISION&o=CURRENT_COMMIT'        
        changes = gerrit_req(dataUrl)
        #print changes
        #if changes:
        detailChangeJson = getJSON_Data(changes)
        if not detailChangeJson == "Error":
            #print detailChangeJson
                # Getting commit message for each changeset
            commit_message = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('message')
                #print commit_message

                #Getting url for each changeset 
            url = 'https://quickoffice-internal.googlesource.com/html-office/+/' + str(detailChangeJson.get('current_revision'))

                #Getting author for each changeset
            author_name = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('author').get('name')

                #Getting author email_id for each changeset
            author_id = detailChangeJson.get('revisions').get(detailChangeJson.get('current_revision')).get('commit').get('author').get('email')
            #print author_name
            try:
                for index,line in enumerate(str(commit_message).splitlines()):
                    #print line
                    if 'BUG' in line:
                        bugs = str(commit_message).splitlines()[index:]
                        #print bugs
                        for bug in bugs:
                            print bug
                            issue_id = 0
                            if not bug.rfind('/') == -1:
                                issue_id = bug[bug.rfind('/')+1:]
                                if issue_id.endswith(','):
                                    issue_id = issue_id[:issue_id.rfind(',')]
                            else:
                                issue_id = bug[bug.rfind('=')+1:]
                            print issue_id
                            jira_summary = authenticateJira_and_getSummary(issue_id)
                            if not jira_summary == "NotValid":
                                #print jira_summary
                                issue_url = "https://issues.quickoffice.com/browse/" + issue_id
                                issue_link = '=hyperlink("' + issue_url + '","' + issue_url + '")'
                                csv_writer.writerow([actual_url, change_id, issue_link, jira_summary])
                            else:
                                csv_writer.writerow([actual_url, change_id, issue_id, "Not a valid jira ID"])
                            if not bug.endswith(',') == 1:
                                break                   
            except Exception, e:
                csv_writer.writerow([actual_url, change_id, "Issue With Commit message", "Issue With Commit Message"])
            
        else:
            csv_writer.writerow([actual_url, change_id, "Issue with Chnage ID, generally occured when user has done cherrypick as same change Id gets generated", ])
        break


def getChange_id(pre_build_no, cur_build_no, build_url):
    json_data = getEntire_Data();
    lists=[]
    lists[:]=range(int(pre_build_no), int(cur_build_no)+1)
    for val in lists:
        actual_url = build_url + str(val)
        print actual_url
        b_soup = BeautifulSoup(urllib2.urlopen(actual_url).read())
        content_div = b_soup.find('div', attrs={'class': 'content'})
        links = content_div.findAll('pre')
        for link in links:
            for line in link:
                if 'Change-Id' in line:
                    change_id = (line[line.rfind(r'Change-Id:')+11:])[:42]
                    #print change_id
                    process_data(change_id, json_data, actual_url)


if __name__ == '__main__':
       # Parsing commandline arguments
    build_url = r'http://build.chromium.org/p/client.chromeoffice/builders/bundle_app/builds/'
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-pre_build', help='Previous Build Number', required=True)
    PARSER.add_argument('-cur_build', help='Current Build Number', required=True)
   
    ARGS = PARSER.parse_args()
    pre_build_no = ARGS.pre_build
    cur_build_no = ARGS.cur_build
    # Handling optional argument build_number
    #create_report_csv()
    getChange_id(pre_build_no, cur_build_no, build_url)

    #getGerritData(pre_build_no, cur_build_no, build_url)