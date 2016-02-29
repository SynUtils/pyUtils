'''
Created on Sep 25, 2014

@author: pavang
'''
import gspread
import csv

SPREADSHEET_NAME = 'test_google_sheet' # google documents spreadsheet name
USERNAME = 'synerzip.qo.pune@gmail.com' # google/gmail login id
PASSWD = 'synerzip123' # google/gmail login password

def login():
    gc = gspread.login(USERNAME, PASSWD)
    wks = gc.open("test_google_sheet").sheet1
    return wks

def get_sheet_data(wks):
#     wks.update_acell('B2', "it's down there somewhere, let me take another look.")
#     print wks.acell('B1').value
#     values_list = wks.col_values(1)
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
            print 'file Name: ' + row[2].strip()
            tmp_list.append(row[4].replace('\x1b','').strip())        
            todays_data.append(tmp_list)  
    return todays_data     
#             print(row[0:3], row[4])

def update_result(google_sheet_data, csv_data, wks):
    column_num = len(google_sheet_data[0])
    print column_num
    for i, row in enumerate(google_sheet_data):
#         print csv_data[i][-1]
#         print 'H'+str(i+1)
        print row[0] +' == '+ csv_data[i][0]
        print row[1] + ' <==> ' + csv_data[i][1]
        if row[0] == csv_data[i][0] and row[1] == csv_data[i][1]:
            wks.update_cell(i+1, column_num+1 , csv_data[i][-1])

if __name__ == '__main__':
    output_file_path = r'/tmp/e2e.csv'
    worksheet = login()
    csv_data = read_csv(output_file_path)
#     print csv_data
    google_sheet_data = get_sheet_data(worksheet)
#     print google_sheet_data
    update_result(google_sheet_data, csv_data, worksheet)
    
#     update_result()
    pass