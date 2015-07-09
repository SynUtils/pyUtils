#!/usr/bin/python
import urllib
import urllib2
import httplib2
import os.path
import zipfile
import xml.etree.ElementTree as ET
import sys
from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

# Email of the Service Account.
SERVICE_ACCOUNT_EMAIL = ('264591438933-s6qukgedsk2ld4gof63pauh7jacvffcg'
                          '@developer.gserviceaccount.com')
# Path to the Service Account's Private Key file.
SERVICE_ACCOUNT_PKCS12_FILE_PATH = '/Users/santoshk/Downloads/key.p12'

BUILD_DICT = dict()
MODIFIED_DATE_LIST = list()
def create_drive_service():
    """Builds and returns a Drive service object authorized 
     with the given service account.

  Returns:
    Drive service object.
  """
    read = file(SERVICE_ACCOUNT_PKCS12_FILE_PATH, 'rb')
    key = read.read()
    read.close()

    credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,
      scope='https://www.googleapis.com/auth/drive')
    http = httplib2.Http()
    http = credentials.authorize(http)
    print http
    return build('drive', 'v2', http=http)

# Get Latest Build
def add_build_to_dict(modified_date, title):
    BUILD_DICT[modified_date] = title
    MODIFIED_DATE_LIST.append(modified_date)
    
# Sort build by modified date
def sort_all_builds():
    MODIFIED_DATE_LIST.sort(cmp=None, key=None, reverse=True)
    
# Download latest build
def download_build(service, drive_file):
    """Download a file's content.
  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
    download_url = drive_file.get('downloadUrl')
    print 'Downloading build ' , drive_file.get('title') , '.....'
    if download_url:
        resp, content = service._http.request(download_url)
        if resp.status == 200:
            #f = resp['content-disposition']
            #date = drive_file.get('userPermission')
            title = drive_file.get('title')
            #print title
            path = '/tmp/'+title
            download_file = open(path, 'wb')
            download_file.write(content)
            print title + " downloaded successfully!!"
        else:
            print 'An error occurred: %s' % resp
    else:
    # The file doesn't have any content stored on Drive.
        print 'Not getting Download URL'
    
# Get files
def print_file(service, file_id):
    """Print a file's metadata.
  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
    try:
        dfile = service.files().get(fileId=file_id).execute()
        if (dfile.get('mimeType') == 'application/zip'):
            title = dfile.get('title')
            title = str(title)
            modified_date = dfile.get('modifiedDate')
            add_build_to_dict(modified_date, dfile)
    except errors.HttpError, error:
        print 'An error occurred: %s' % error

# Geting all child element in shared folder        
def print_files_in_folder(service, folder_id):
    """Print files belonging to a folder.
  Args:
    service: Drive API service instance.
    folder_id: ID of the folder to print files from.
  """
    page_token = None
    while True:
        try:
            param = {}	
            if page_token:
                param['pageToken'] = page_token
            children = service.children().list(
                folderId=folder_id, **param).execute()
            #item = children.get('items')
            print 'Please Wait...While getting latest build number..'
            for child in children.get('items'):
                print_file(service, child['id'])
            page_token = children.get('nextPageToken')
            if not page_token:
                break
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
        break
    
# Method to call download google shared build
def google():
    service = create_drive_service()
    folder_id = '0B1e329gGpJk1eVdtNFRJcDMwSVE'
    print_files_in_folder(service, folder_id)
    sort_all_builds()
    print 'Latest build is' , BUILD_DICT.get(MODIFIED_DATE_LIST[0]).get('title')
    download_build(service, BUILD_DICT.get(MODIFIED_DATE_LIST[0]))

#Getinng previous build number which is downloaded already
def get_previous_build_number(file_name):
    pre_file = open(file_name, 'r')
    prev = pre_file.readline()
    return prev

#Compare previous and latest build number
def compare_build_numbers(prev, new):
    if prev != new:
        return 1
    else:
        print ("We already ran c2c on this build. "
        "There is no new build generated.")
        return 0

#Write build number in txt file
def write_build_number(file_name, number):
    build_file = open(file_name, 'wb')
    build_file.write(number)

#Extract downloaded latest build
def extract_zip(zip_file_path, number):
    os.makedirs("/tmp/" + number)
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall("/tmp/" + number + "/")
   
#copy extacted build to destination folder
def copy_crx(number):
    txt_file = open("c2cprop.txt","r")
    path = txt_file.readline().rstrip("\n")
    path = path.split(":")
    dest_path = "".join(path[1]).rstrip("\n")
    crx_path = dest_path + "/app/"
    cmd = 'cp -rf /tmp/' + number + '/*' + ' ' + crx_path
    os.system(cmd)
    print "Build copied successfully!"

# Function to download latest bamboo build
def download_build_master(number):
    url_txt = 'http://quickbuild.quickoffice.com/browse/HOSGCMASTER-EDIT-' +\
     number +\
      '/artifact/GCANVIEWCRXZIP/Zipped-web-app/quickoffice-chrome-1.1.1.' +\
       number + '.zip'
    print url_txt
    num = 'quickoffice-chrome1.1.1.'
    path = '/tmp/' + num + number + '.zip'
    print path
    print '############ Downloading build ###################'
    urllib.urlretrieve(url_txt, path)
    print  '########### Build Downloaded #####################'
    #extract_zip(path, number)
    #copy_crx(number)

#Function to call download latest master build from bamboo    
def master():
    build_file = "buildNumber.txt"
    url = urllib2.Request('http://quickbuild.quickoffice.com/rest/api/'
                          'latest/result/HOSGCMASTER-EDIT?'
                          'expand=results.result.artifacts')
    response = urllib2.urlopen(url)
    the_page = response.read()
    root = ET.fromstring(the_page)
    child = root[0][0].tag
    for child in root:
        for result in child.findall('result'):
            name = result.get('state')
            if name == 'Successful':
                number = result.get('number')
                print "latest successful build : " + number
                if os.path.exists(build_file) :
                    prevbuildnumber = get_previous_build_number(build_file)
                    print "Previous master build : " + prevbuildnumber
                    if compare_build_numbers(prevbuildnumber, number):
                        download_build_master(number)
                        write_build_number(build_file, number)
                else:
                    download_build_master(number)
                    write_build_number(build_file, number)
                break
#Check if argument pass or not
if not len(sys.argv) > 1 :
    print "please pass argument"
else :
    MODE = sys.argv[1]
    if MODE == 'GOOGLE':
        google()
    else:
        if MODE == 'MASTER':
            master()
        else:
            print "Wrong Argument Please pass GOOGLE OR MASTER"
        
        




