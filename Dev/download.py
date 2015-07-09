'''
Created on Sep 10, 2014

@author: pavang
'''
#!/usr/bin/python
import urllib
import urllib2
from bs4 import BeautifulSoup
import argparse
import subprocess
import os
import zipfile
BUILD_FILE = 'buildNumber.txt'

def extract_zip(zip_file_path, number):
    """
    Extract files
    Args :
    zip_file_path : zip file path instance
    """
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        cmd = 'mkdir ' + number
        os.system(cmd)
        zip_file.extractall('/tmp/' + number)
        zip_file.close()
def extract_and_move(path, number):
    """
    Common method for extracting and coping build
    Args:
    path : Extract file path instance
    BUILD_FILE : build file instance
    number : build number instance
    """
    extract_zip(path)
    #copy_crx()
    write_build_number(BUILD_FILE, number)

def write_build_number(file_name, number):
    """
    Write build number in buildNumber.txt file
    Args:
    file_name : File name instance
    number : build number instance
    """
    build_file = open(file_name, 'wb')
    build_file.write(number)
    build_file.close()

def get_previous_build_number(file_name):
    """
    Function gives previous build number which is downloaded already
    Args:
    file_name : File name instance
    Return :
    Return build number
    """
    print 'in build'
    pre_file = open(file_name, 'r')
    prev = pre_file.readline()
    pre_file.close()
    return prev


def compare_build_numbers(prev, new):
    """
    Compare previous and latest build number
    Args:
    prev : Previous build number instance
    new : New build number instance
    Return:
    Return true or false (1 or 0)
    """
    if prev != new:
        return 1
    else:
        return 0

def download_build(url, number, build):
    cmd = 'gsutil cp ' + url.replace("https://storage.cloud.google.com/", "gs://", 1) + ' ' + '/tmp/'
    print "command is.... " + cmd
    os.system(cmd)
    path = '/tmp/' + 'quickoffice-chrome-0.0.0.' + number + '_' + build + '.zip'
    print  path
    extract_zip(path, number)

    write_build_number(BUILD_FILE, number)

def download_asan(url):
    cmd = 'gsutil cp ' + url.replace("https://storage.cloud.google.com/", "gs://", 1) + ' ' + '/tmp/'
    os.system(cmd)

def get_latest_buid(url, download_url,build):
    flag =1
    print 'url in build number ' + url
    print 'url in build number ' + download_url
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    table = soup.find('div', attrs={'class': 'content'})
    rows = table.findAll('tr')

    for tr in rows:
        for td in tr:
            if 'success' in td:
                flag = 0

        if flag == 0:
            break
        else:
            continue

    a = tr.findAll('a')
    print a
    BS = BeautifulSoup(str(a))
    num = BS.a.contents[0].strip()[1:]
    print num
    if (build == 'pasan'):
        download_url = download_url + num + '/testing/point/PointDCPSA-asan'
    elif(build == 'sasan'):
        if (MODE == 'MASTER'):
            download_url = download_url + num + '/testing/sheet/asan'
        else:
            download_url = download_url + num + '/testing/pronto-sheet/asan'


    elif(build == 'wasan'):
        download_url = download_url + num + '/testing/word/asan'
    else:
        download_url = download_url + num + '/quickoffice-chrome-0.0.0.' + num + '_' + build + '.zip'
    print 'BUILD Download:----- ' + download_url

    if (build in lst_asan):
        download_asan(download_url)
    else:
        download_build(download_url, num, build)



    #download_build(download_url, num, build)

    #if os.path.exists(BUILD_FILE):
    #    prev_build_number = get_previous_build_number(BUILD_FILE)
    #    print "Previous master build : " + prev_build_number
    #    if compare_build_numbers(prev_build_number, num):
    #        download_build(download_url, num, build)
    #    else:
    #        print ("""We already ran c2c on this build.
    #                    There is no new build generated.""")
    #else:
    #    download_build(download_url, num, build)


if __name__ == '__main__':
    lst_build =['cwsExt','cwsInt','compExt','debug', 'srcMap']
    lst_asan = ['pasan', 'sasan', 'wasan']

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('Mode', help='Mode to download build MASTER/PRONTO')
    PARSER.add_argument('Build', help='cwsExt/cwsInt/compExt/debug/pasan/wasan/sasan')
    ARGS = PARSER.parse_args()
    MODE = ARGS.Mode
    BUILD = ARGS.Build
    print 'hi'
    if (MODE == 'MASTER' and BUILD in lst_asan or BUILD in lst_build):
        print 'master'
        url = 'http://build.chromium.org/p/client.quickoffice/builders/Master/'
        new_url = 'http://build.chromium.org/p/client.chromeoffice/builders/bundle_app'
        download_url = 'https://storage.cloud.google.com/chrome-quickoffice/master/0.0.0.'
    elif (MODE == 'PRONTO' and BUILD in lst_build or BUILD in lst_asan):
        url = 'http://build.chromium.org/p/client.quickoffice/builders/Master_Pronto-Sheet/'
        download_url = 'https://storage.cloud.google.com/chrome-quickoffice/master_pronto-sheet/0.0.0.'
    else :
        print "Wrong Argument please pass MASTER/PRONTO for Mode and cwsExt/cwsInt/compExt/debug/pasan/sasan/wasan for builds"
        print PARSER.print_help()

    get_latest_buid(url, download_url, BUILD)






