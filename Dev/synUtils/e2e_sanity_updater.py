'''
Created on Sep 25, 2014

@author: pavang
'''
import gspread
import csv
import os
import datetime
import time

def login(user_name, password, file_name, sheet_name):
    gc = gspread.login(user_name, password)
    wks = gc.open(file_name)
    worksheet = wks.worksheet(sheet_name)
    return worksheet

def get_sheet_data(wks):
    list_of_lists = wks.get_all_values()
    return list_of_lists

def read_csv(input_file):
#     row_dict = { "id": "0", "title": "Pavan", "totaldefect": "HelloMrDJ" }
    with open(input_file) as csv_file:
        todays_data = []        
        file_data = csv.reader(csv_file)        
        for row in file_data:
            tmp_list = []
            tmp_list.append(row[0].strip())
            tmp_list.append(row[1].strip())
#             print 'Inserting file Name: ' + row[2].strip()
            tmp_list.append(row[2].strip())
            tmp_list.append(row[4].replace('\x1b','').strip())        
            todays_data.append(tmp_list)  
    return todays_data     
#             print(row[0:3], row[4])

def process_log(input_file_path, output_file_path):
    """
    reads e2e logs from file, parsed it and write results in 
    """
    with open(output_file_path,'w') as csv_file:
        spec_result = ''
        _file = ''
        suite = ''
        spec = ''
        failed_text = ''
        csv_writer = csv.writer(csv_file, delimiter = ',')
        csv_writer.writerow(['suite', 'spec', 'file', 'Error', 'spec_result'])         
        if os.path.isfile(input_file_path):            
            for line in open(input_file_path).readlines():
                line = str(line)
                final_text = line[line.find(':') + 1 :]
                if line.find('Spec result:') >= 0:
                    spec_result = final_text[:final_text.find('[')]
                if line.find('File:') >= 0:
                    _file = final_text
                if line.find('Suite:') >= 0:
                    suite = final_text
                if line.find('Spec:') >= 0:
                    spec = final_text 
                if line.find('Assertion 1') >= 0:
                    failed_text = final_text
                print(line) 
                if spec_result and _file and suite and spec:
                    if spec_result.find('failed') >= 0 and failed_text == '':
                        continue                                        
                    csv_writer.writerow([suite, spec, _file,  failed_text, spec_result])
                    spec_result = _file = suite = spec= failed_text= ''

def devide_list_by_file_type(list_of_list_data, list_doc_docx, list_xls_xlsx, list_ppt_pptx):  
    for i, _list in enumerate(list_of_list_data):
        file_ext = _list[2][_list[2].rfind('.') + 1:]
        if file_ext in ['xls', 'xlsx']:
            list_xls_xlsx.append(_list)            
        elif file_ext in ['ppt', 'pptx']:
            list_ppt_pptx.append(_list)
        elif file_ext in ['doc', 'docx']:
            list_doc_docx.append(_list)
#         print _list[2] + '------------' + file_ext
#     print list_ppt_pptx
    pass

def update_result(google_sheet_data, csv_data, wks):
    column_num = len(google_sheet_data[0])
    wks.add_cols(1)
    wks.update_cell(1, column_num+1, str(time.strftime("%d/%m/%Y")))
    print column_num
    for i, row in enumerate(google_sheet_data):
#         print csv_data[i][-1]
#         print 'H'+str(i+1)
        if i == 0:
            continue
        print row[0] +' <==> '+ csv_data[i-1][0]                              #suite
        print row[1] + ' <==> ' + csv_data[i-1][1]                            #spec
        print row[2] + ' <==> ' + csv_data[i-1][2]                            #file
        print '-' * 100
        
        if row[0] == csv_data[i-1][0] and row[1] == csv_data[i-1][1] and row[2] == csv_data[i-1][2]:
            wks.update_cell(i+1, column_num+1 , csv_data[i-1][-1])

if __name__ == '__main__':
    SPREADSHEET_NAME = 'test_google_sheet' # google documents spreadsheet name
    USERNAME = 'synerzip.qo.pune@gmail.com' # google/gmail login id
    PASSWD = 'synerzip123' # google/gmail login password
    input_file_path = r'/tmp/pavan.log'
    output_file_path = r'/tmp/e2e.csv'
    list_doc_docx = []
    list_xls_xlsx = []
    list_ppt_pptx = []
    
    process_log(input_file_path, output_file_path)
    csv_data = read_csv(output_file_path)
    devide_list_by_file_type(csv_data, list_doc_docx, list_xls_xlsx, list_ppt_pptx)
#     print list_xls_xlsx
#     print list_doc_docx
#     print csv_data
    worksheet = login(USERNAME, PASSWD, SPREADSHEET_NAME, 'qw')
    google_sheet_data = get_sheet_data(worksheet)
    update_result(google_sheet_data, list_doc_docx, worksheet)
    
    print '=' * 30 + '           Updating Sheet data           ' + '=' * 30
    
    worksheet = login(USERNAME, PASSWD, SPREADSHEET_NAME, 'qs')
    google_sheet_data = get_sheet_data(worksheet)
    update_result(google_sheet_data, list_xls_xlsx, worksheet)
    pass
