from __future__ import print_function
'''
Created on Sep 11, 2014

@author: pavang
'''
# dependency 
# sudo pip install gsutil
# sudo pip install beautifulsoup4

"""
to do: 

"""

from bs4 import BeautifulSoup
import urllib2
import os
import argparse

internal_build_num = 0

def download_build(url, build_type, build_name = 'master', output_directory = '/tmp/'):
    """
    downloads build using gsutil cp command
    """
#https://console.developers.google.com/storage/browser/chrome-quickoffice/waterfallv2/master/0.0.0.262/bundle_app/
# gsutil cp gs://chrome-quickoffice/waterfallv2/master/0.0.0.276/bundle_app/quickoffice-chrome-0.0.0.276_debug.zip

    new_artifact_name =''
    if build_name == 'master':
        url = url + '/bundle_app/quickoffice-chrome-' + internal_build_num + '_' + build_type + '.zip'
    elif build_name == 'wasan':
        url = url + '/word/asan'
        new_artifact_name = '_word_' + internal_build_num
    elif build_name == 'sasan':
        url = url + '/sheet/asan'
        new_artifact_name = '_sheet_' + internal_build_num
    elif build_name == 'pasan':
        url = url + '/point/asan'
        new_artifact_name = '_point_' + internal_build_num
    elif build_name == 'wrt':
        url = url + r'/word/core-saver-docx-test'
        new_artifact_name = '_word_' + internal_build_num
    elif build_name == 'srt':
        url = url + r'/sheet/cmd-line'
        new_artifact_name = '_sheet_' + internal_build_num
    elif build_name == 'prt':
        url = url + r'/point/round-trip'
        new_artifact_name = '_point_' + internal_build_num
    else:
        print("Incorrect Build Name: "+ build_name)
    
    cmd = 'gsutil cp ' + url + ' ' + output_directory
    os.system(cmd)
    new_artifact_name = url[url.rfind('/') + 1:] + new_artifact_name
#     new_artifact_name = os.path.join(output_directory, new_artifact_name)
    os.rename(os.path.join(output_directory, url[url.rfind('/') + 1:]), os.path.join(output_directory, new_artifact_name))
    print('Build download at: '+ os.path.join(output_directory, new_artifact_name))

def get_version_build_type(internal_build_num,version_type):
    """""
    return version type with build number. 
    """""
    if ('0.0.0')in str(internal_build_num):
        version_type = 'master/'
    else:
        parent_build_num = internal_build_num[:internal_build_num.rfind(r'.')]
        version_type =  version_type + parent_build_num + '/'
    return version_type


def get_buid_url(external_url, download_url, build_type,version_type):
    """
    return build url with build number.
    """
    global internal_build_num
    if internal_build_num:
        version_type = get_version_build_type(internal_build_num,version_type)
        print("Internal Build Number: " + internal_build_num)
        download_url = download_url + str(version_type) + str(internal_build_num)
    else:        
        flag =1
        soup = BeautifulSoup(urllib2.urlopen(external_url).read())
        table = soup.find('div', attrs={'class': 'content'})
        rows = table.findAll('tr')
        for tr in rows:
            for td in tr:
                if 'success' in td:
                    flag = 0    
            if flag == 0:
                a = tr.findAll('a')
                bs = BeautifulSoup(str(a))
                num = bs.a.contents[0].strip()[1:]
                print("External Build Number: " + num)
                break
            else:
                continue                    
        internal_url = external_url + '/builds/' + str(num)
        # taking build_type num from internal URL
        b_soup = BeautifulSoup(urllib2.urlopen(internal_url).read())
        content_div = b_soup.find('div', attrs={'class': 'content'})
        links = content_div.findAll('a')
        for link in links:
            link = str(link)
            build_str = '_' + build_type + r'.zip'
            if build_str in link:
                link = link[:link.rfind(build_str)]
                internal_build_num = link[link.rfind(r'-') + 1 :]
                print("Internal Build Number: " + internal_build_num)
                version_type = get_version_build_type(internal_build_num,version_type)
                break
        download_url = download_url + str(version_type) + internal_build_num 
    # Sample Download URL
    # https://console.developers.google.com/storage/chrome-quickoffice/waterfallv2/master/0.0.0.262/bundle_app/ quickoffice-chrome-0.0.0.262_debug.zip
    return download_url
#     print(flag)

if __name__ == '__main__':
    retry = 0
    isException= 0 
    lst_build_type =['debug','cwsExt','cwsInt','compExt', 'srcMap']
    lst_build_name = ['master', 'wasan', 'sasan', 'pasan', 'wrt', 'srt', 'prt']
    external_url = r'http://build.chromium.org/p/client.chromeoffice/builders/bundle_app'
    internal_url = r'http://build.chromium.org/p/client.chromeoffice/builders/bundle_app/builds/'
    download_url = r'gs://chrome-quickoffice/waterfallv2/'
    version_type = 'releases/'
    # Parsing commandline arguments
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('build_type', default = 'debug', choices = lst_build_type, help='Type of build you want to download, its an optional argument with default value "debug"', nargs='?')
    PARSER.add_argument('build_name', default = 'master', choices = lst_build_name, help='Name of the buid, its an optional argument with default value "master"', nargs='?')
    PARSER.add_argument('build_number', help='Optional argument to specify build number', nargs='?')
    ARGS = PARSER.parse_args()
    BUILD_TYPE = ARGS.build_type 

    # Handling optional argument build_number
    if ARGS.build_number:
        if ('0.0.0') in ARGS.build_number:
            version_type = 'master/'
        internal_build_num = ARGS.build_number
    # Note: get_buid_url method uses internal_build_num
    while (retry < 3):
            try:    
                build_url = get_buid_url(external_url, download_url, BUILD_TYPE,version_type)
                if ARGS.build_name.lower() in lst_build_name:
                    download_build(build_url, BUILD_TYPE, ARGS.build_name.lower())
                    break;
            except:
                isException=1
                retry=retry + 1    
#     download_master_build(build_url, BUILD_TYPE)    
    pass