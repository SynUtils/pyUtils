#!/usr/bin/python
#
#
#  1) Install the google documents python api
#  2) Create a spreadsheet in google documents and save it under a name
#     that matches SPREADSHEET_NAME
#  3) Name the column headings of the google spreadsheet 'id','date','time'
#  4) Edit USERNAME and PASSWD to match your login info
#  5) Make this file executable
#  6) In a terminal window, type 'crontab -e' and add this script to your
#

import os
import gdata.spreadsheet.service
# import time,string
## Change These to Match Your Info!

SPREADSHEET_NAME = 'test_google_sheet' # google documents spreadsheet name
USERNAME = 'synerzip.qo.pune@gmail.com' # google/gmail login id
PASSWD = 'synerzip123' # google/gmail login password
# BASE_DIR = '/tmp/' # Base Directory to locally save your IP info
                   # trailing slash required!
# IP_WEBSITE = 'www.whatismyip.org'
## Function Definitions
def StringToDictionary(row_data):
  result = {}
  for param in row_data.split():
    name, value = param.split('=')
    result[name] = value
  return result

def load():
  gd_client = gdata.spreadsheet.service.SpreadsheetsService()
  gd_client.email = USERNAME
  gd_client.password = PASSWD
  gd_client.ProgrammaticLogin()
  print '****   Hurray authentication done!!! for User name: '+ gd_client.email
  return gd_client


def insert_data(row_dict):
    gd_client = load()
    print ' ***  I am in Gspeardsheets ***'
    docs= gd_client.GetSpreadsheetsFeed()
    spreads = []
    for i in docs.entry: 
        spreads.append(i.title.text)
        print i.title.text
        if i.title.text == SPREADSHEET_NAME:
            break;
    for i, sheet in enumerate(spreads):
        if sheet == SPREADSHEET_NAME:
            sheet_num = i
            print sheet_num
            break;
    key = docs.entry[sheet_num].id.text.rsplit('/', 1)[1]
    print key
    feed = gd_client.GetWorksheetsFeed(key)
    wksht_id = feed.entry[0].id.text.rsplit('/', 1)[1]
    print wksht_id
#     entry = gd_client.InsertRow(row_dict, key, wksht_id) 
    gd_client.UpdateCell(2, 2, "UpdatedCell", key)
    print gd_client.GetCellsFeed(key, wksht_id, "R2C3")
#     print entry

if __name__ == '__main__':
    
    row_dict = { "id": "0", "title": "Pavan", "totaldefect": "HelloMrDJ" }
    insert_data(row_dict)
            
#         
# def updateIP(ip):
#   gd_client = load()
#   print ' ***  I am in Gspeardsheets ***'
#   docs= gd_client.GetSpreadsheetsFeed()
#   spreads = []
#   for i in docs.entry: 
#       spreads.append(i.title.text)
#       print i.title.text
#   print ' ****   This is the gspeardsheet Nmae ****    '
#   print '   SPREADSHEET_NAME    '  +SPREADSHEET_NAME
#   spread_number = None
#   for i,j in enumerate(spreads):
#     if j == SPREADSHEET_NAME: spread_number = i
#   if spread_number == None:
#     return 0
# 
#   key = docs.entry[spread_number].id.text.rsplit('/', 1)[1]
#   feed = gd_client.GetWorksheetsFeed(key)
#   wksht_id = feed.entry[0].id.text.rsplit('/', 1)[1]
#   feed = gd_client.GetListFeed(key,wksht_id)
#   #print feed
#   thetime = time.strftime('%I:%M%p')
#   thedate = time.strftime('%m/%d/%y')
# 
#   print '**** I am about to read in gdoc ****'
#   row = { "id": "0", "title": "Sheetal","totalDefect": "119" }	
#   print row
#   entry = gd_client.InsertRow(row, key, wksht_id)   
#   return 1


## Executed Code
# if __name__ == '__main__':
#     row_dict = { "id": "0", "title": "Sheetal","totalDefect": "119" }
#     insert_data(row_dict)
#     if os.path.exists(BASE_DIR+'CheckIP'): 
#         os.remove(BASE_DIR+'CheckIP')
# #     os.system('wget '+IP_WEBSITE+' -t 2 --output-document='+BASE_DIR+'CheckIP')
# #     fh2 = open(BASE_DIR+'CheckIP','r')
# #     ip2 = fh2.read()
# #     fh2.close()
#     
#     if os.path.exists(BASE_DIR+'CurrentIP'):
#       fh1 = open(BASE_DIR+'CurrentIP','r')
#       ip1 = fh1.read()
#       fh1.close()
#     else:
#       ip1 = ''
#     res = updateIP(ip2)
#     if res == 0: 
#     	print 'hi'
#     	#raise 'Please Create a Spreadsheet named \''+SPREADSHEET_NAME+'\' in googleDocs.'
#     else:
#     	fh = open(BASE_DIR+'CurrentIP','w')
#     	fh.write(ip2)
#     	fh.close()
#         
        
        