import csv

def update_csv(input_path='/tmp/Jira_Mapping.csv', output_path='/tmp/Updated_Jira_Mapping.csv'):
	severity = ['crash', 'dataloss', 'incorrectlyfunctioning']
	recurrence = ['alwaysrepro', 'intermittent']
	type_bug = [r'Type-Bug-Regression']
	module = ['Point', 'Word', 'Sheet']
	priority = [r'Pri-0', 'Pri-1', 'Pri-2', 'Pri-3 ']

	columns = [severity, recurrence, type_bug, module, priority]
    op

	with open(input_path) as input_file, open(output_path,'w') as output_file:
		csv_writer = csv.writer(output_file)
		csv_writer.writerow(['AllLabels', 'severity', 'recurrence', 'type_bug', 'module', 'priority'])
		for i, row in enumerate(input_file):
			# print str(row)
			# row_list =  str(row).replace(r'Cr-Platform-Apps-Default-ChromeOffice-','\nCr-Platform-Apps-Default-ChromeOffice-')
			# print i, str(row) + '   ---->   ' + row_list
			flag = False
			new_row = row 
			for col in columns:
				flag = False
				for item in col:
					if item in row:
						new_row = new_row + ',' + item
						flag = True
						break
				if not flag:
					new_row = new_row + ','


			print new_row
			csv_writer.writerow(new_row.split(','))
			

if __name__ == '__main__':
	update_csv(input_path='/tmp/build_perf_compare.csv')
