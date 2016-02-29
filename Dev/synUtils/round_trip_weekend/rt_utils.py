'''
* Copyright 2013 Google Inc. All Rights Reserved.
 * @fileoverview : RT automation utilities for
 * word , sheet & point.Utility file contains all
 * functions required to automated roundtrip procedure
 * of word [.doc/.docx] ,Sheet[.xlsx] & point [.pptx] files
 * @author jayashree.patil@synerzip.com (Jayashree Patil)
*'''

import sys
import datetime
import os
import errno
import traceback
import subprocess
import time
import distutils.file_util
import argparse
import stat

TODAYS_DATE = str(datetime.datetime.now()).split(' ')
INPUT_TEST_FILES_PATH = ''
RT_EXE = ''


def create_directory():
    ''' @Description :  Creates all required directories  '''
    try:
        dir_list = {'toplevel_dir': '', 'round_trip_folder': '',
                    'log_folder': '', 'crash_folder': '', 'invalid_folder': '',
                    'original_moved': '', 'failed_to_rt': '', 'timeout': '',
                    'point_test_data_path': ''}
        dir_list['toplevel_dir'] = '{0}result_{1}'.format(INPUT_TEST_FILES_PATH,
                                                          TODAYS_DATE[0])
        dir_list['round_trip_folder'] = '{0}/RT/'.format(
            dir_list['toplevel_dir'])
        dir_list['log_folder'] = '{0}/logs/'.format(dir_list['toplevel_dir'])
        dir_list[
            'crash_folder'] = '{0}/crash/'.format(dir_list['toplevel_dir'])
        dir_list['invalid_folder'] = '{0}/invalid/'.format(
            dir_list['toplevel_dir'])
        dir_list['original_moved'] = '{0}/original_moved/'.format(
            dir_list['toplevel_dir'])
        dir_list['failed_to_rt'] = '{0}/failed_to_rt/'.format(
            dir_list['toplevel_dir'])
        dir_list['timeout'] = '{0}/timeout/'.format(dir_list['toplevel_dir'])
        dir_list[
            'point_test_data_path'] = 'test/test_data/point/unit_test_data'
        print dir_list
        if not os.path.exists(dir_list['toplevel_dir']):
            os.makedirs(dir_list['toplevel_dir'])
            os.makedirs(dir_list['round_trip_folder'])
            os.makedirs(dir_list['log_folder'])
            os.makedirs(dir_list['crash_folder'])
            os.makedirs(dir_list['original_moved'])
            os.makedirs(dir_list['invalid_folder'])
            os.makedirs(dir_list['failed_to_rt'])
            os.makedirs(dir_list['timeout'])
        return dir_list
    except OSError as err:
        if err.errno == errno.EEXIST:
            print 'Warning: Directory already exists'
            return dir_list
        elif err.errno == errno.EACCES:
            sys.exit('Error: Directory cannot be created , Permissions denied')


def create_point_directories(test_files_path, dir_list):
    ''' @Description :  Creates directory path for point files
        Note : Need to create directory path "test_data/point/unit_test_data"
        explicitly as it is hard coded in headless utility of point in
        a such a way that it takes file for roundtriping from
        "unit test data" folder & roundtrip it'''
    try:
        if not os.path.exists(dir_list['point_test_data_path']):
            os.makedirs(dir_list['point_test_data_path'])
            print ' Path for point files has been created successfully'
 #       ppt_original_files_path = ("{0}/original_moved_pptx_files"
 #                           .format(dir_list["toplevel_dir"]))
 #       os.makedirs(ppt_original_files_path)
        subprocess.call(['chmod', '0777', test_files_path])
        if str(test_files_path)[-1] != '/':
            test_files_path = test_files_path + '/'
        if get_files() != 0:
          #          cmd = ("{0} -type f | cp {1}* {2}"
          #          .format(test_files_path, test_files_path, ppt_original_files_path))
          #          print "::::::::::1"+cmd
          #          os.system(cmd)
            cmd = ('{0} -type f | cp {1}* {2}'.format(test_files_path,
                                                      test_files_path, dir_list['point_test_data_path']))
            print '::::::::::2' + cmd
            os.system(cmd)
    except OSError:
        if OSError.errno == errno.EACCES:
            sys.exit('Error: Directory %s '
                     'cannot be created , Permissions denied'
                     % (dir_list['point_test_data_path']))
        if OSError.errno == errno.EEXIST:
            print 'Warning: Directory already exists'
        else:
            traceback.print_exc()


def check_command_status(file_name, rt_command, time_out, dir_list):
    ''' @Description :  check for rt command status & timeout of rt processing
        if roundtripping takes more time than specified time(in seconds) ,
        move to next file processing'''
    rt_process = subprocess.Popen(rt_command, shell=True)
    time_count = 0
    while time_count < time_out and rt_process.poll() is None:
        time.sleep(1)
        time_count += 1
    if rt_process.poll() is None:
        rt_process.terminate()
        print 'Timeout occured while executing rt command'
        move_timeout_file(file_name, dir_list)
        return None
    else:
        return rt_process.poll()


def arg_parse():
    ''' @Description :  Parse command line arguments with help information'''
    parser = argparse.ArgumentParser(description='RT automation script')
    parser.add_argument('-binary', action='store', dest='headless_utility',
                        help='headless utility of word/sheet/point',
                        required=True)
    parser.add_argument('-input_files', action='store', dest='test_data_folder',
                        help='Folder containing test files',
                        required=True)
    try:
        args = parser.parse_args()
        # -- Show entered command line arguments
        print'You entered following inputs to perform RT'
        print ('Headless utility : %s' % args.headless_utility)
        print ('Test data folder : %s' % args.test_data_folder)
        return args
    except SystemExit:
        print('Invalid no. of arguments \n Type '
              "'python rtAutomation_main.py -h' for usage info")
        sys.exit()


def init():
    ''' @Description :  Checks argument list & initializes required variable
        for RT process '''
    args = arg_parse()
    global INPUT_TEST_FILES_PATH
    INPUT_TEST_FILES_PATH = args.test_data_folder
    if str(INPUT_TEST_FILES_PATH)[-1] != '/':
        INPUT_TEST_FILES_PATH = '{0}/'.format(args.test_data_folder)
    global RT_EXE
    RT_EXE = args.headless_utility
    directories = create_directory()
    if 'PointCommandTest' in RT_EXE:
        os.system('chmod a+x ' + RT_EXE)
        create_point_directories(INPUT_TEST_FILES_PATH, directories)
    if 'core_saver_docx' in str(RT_EXE):
        distutils.file_util.copy_file(RT_EXE, 'core_saver_docx_test')
        os.system('chmod a+x core_saver_docx_test')
        RT_EXE = 'core_saver_docx_test'
    else:
        os.system('chmod a+x ' + RT_EXE)
    #--- Create .csv to store roundtrip results
    try:
        fname = 'RoundTripResults.csv'
        file_handle = open(directories['toplevel_dir'] + '/' + fname, 'a')
        return file_handle, directories
    except IOError:
        print'-- Error while creating .csv file ---'
        traceback.print_exc()
        sys.exit()


def get_files():
    ''' @Description :  Returns list of files in a given directory '''
    test_files = os.listdir(INPUT_TEST_FILES_PATH)
    if len(test_files) == 0:
        print 'There are no input files'
        return 0
    else:
        return test_files


def write_file_header(file_handle):
    '''
        @Description :  Writes header for result.csv
        @param : {File Object} File Object
    '''
    try:
        file_handle.write('File Name, Original File Size(Kb),'
                          ' Roundtrip File Size(Kb),File Size Difference After RT(Kb),'
                          ' Time Required(Min:Sec),Start Time, End Time,\n')
        file_handle.flush()
    except IOError as err:
        print err
        sys.exit('Error occured while writing header to .csv')


def get_empty_row():
    ''' @Description : Returns empty row in dictionary structure '''
    empty_row = {'File Name': '', 'O_File_Size': '', 'R_File_Size': '',
                 'File Size Difference After RT': '', 'Time Required': '', 'Start Time': '', 'End Time': ''}
    return empty_row


def write_row(file_handle, row):
    '''
        @Description :  Writes row to .CSV
        @param : {File Object, dictionary}
                 File Object , Dictionary of .csv headers
    '''
    row['File Name'] = row['File Name'].replace(',', ' ').strip()
    row['O_File_Size'] = row['O_File_Size']
    row['R_File_Size'] = row['R_File_Size']
    row['File Size Difference After RT'] = row['File Size Difference After RT']
    row['Time Required'] = row['Time Required']
    row['Start Time'] = row['Start Time']
    row['End Time'] = row['End Time']
    print row
    try:
        file_handle.write('%(File Name)s, %(O_File_Size)s, %(R_File_Size)s,'
                          '%(File Size Difference After RT)s, %(Time Required)s, %(Start Time)s, %(End Time)s\n ' % row)
        file_handle.flush()
    except IOError as err:
        print 'Error occurred while writing data to .csv', err


def get_current_time():
    ''' @Description : Returns current system time '''
    return datetime.datetime.now()


def get_time_diff(start_time, end_time):
    '''
    @Description : Calculates roundtriping time of a file and return in
                   min:sec format
    @param : {DateTime} Start time , End time .timetuple()'''
    s_time = time.mktime(start_time.timetuple())
    e_time = time.mktime(end_time.timetuple())
    time_diff = e_time - s_time
    if time_diff > 60:
        min_val = time_diff / 60
        sec_val = time_diff % 60
    else:
        min_val = 00
        sec_val = time_diff
    print 'Time difference ::', sec_val
    return str(min_val) + ':' + str(sec_val)


def get_file_size(file_path):
    '''
    @Description : Calculates file size in KB
    @param : {String} File name '''
    try:
        return os.path.getsize(file_path) / 1000.00
    except OSError as err:
        print('Error:%s' % (err))


def get_rt_file_path(file_name, dir_list):
    '''
    @Description : Returns RT file path
    @param : {String} File name '''
    if get_file_extension(file_name) in('xlsx', 'xls'):
        rt_file_name = dir_list['round_trip_folder'] + file_name
    elif get_file_extension(file_name) in('doc', 'docx'):
        rt_file_name = INPUT_TEST_FILES_PATH + get_rt_file_name(file_name)
    else:
        rt_file_name = INPUT_TEST_FILES_PATH + file_name
    return rt_file_name


def get_rt_command(file_name, dir_list):
    '''
    @Description : Constructs RT command for word & sheet files
    @param : {String} File name '''
    file_ext = get_file_extension(file_name)
    print 'File ext is ', file_ext
    log_file_name = "'{0}{1}_log.txt'".format(dir_list['log_folder'],
                                              file_name)
    err_file_name = "'{0}{1}_error.txt'".format(dir_list['log_folder'],
                                                file_name)
    if file_ext in('doc', 'docx'):
        rt_file_name = "'{0}{1}'".format(INPUT_TEST_FILES_PATH, file_name)
        if RT_EXE[0] != '/':
            rt_command = ('./{0} {1} --apply-defaults >{2} 2>{3}'
                          .format(RT_EXE, rt_file_name,
                                  log_file_name, err_file_name))
        else:
            rt_command = ('{0} {1} --apply-defaults >{2} 2>{3}'
                          .format(RT_EXE, rt_file_name,
                                  log_file_name, err_file_name))
        print 'RT Command for doc/docx is :', rt_command
        return rt_command
    elif file_ext in('xls', 'xlsx'):
        rt_file_name = "'{0}{1}'".format(dir_list['round_trip_folder'],
                                         file_name)
        if RT_EXE[0] != '/':
            rt_command = ("./{0} --roundtrip {1}'{2}' {3} >{4} 2>{5}"
                          .format(RT_EXE, INPUT_TEST_FILES_PATH, file_name,
                                  rt_file_name, log_file_name, err_file_name))
        else:
            rt_command = ("{0} --roundtrip {1}'{2}' {3} >{4} 2>{5}"
                          .format(RT_EXE, INPUT_TEST_FILES_PATH, file_name,
                                  rt_file_name, log_file_name, err_file_name))
        print 'Sheet RT Command is :', rt_command
        return rt_command
    elif file_ext == 'pptx':
        if RT_EXE[0] != '/':
            rt_command = ('./{0} {1} --gtest_filter='
                          'AutomationTest.AutoSaveMultipleFilesTest >{2} 2>{3}'
                          .format(RT_EXE, file_name, log_file_name, err_file_name))
        else:
            rt_command = ('{0} {1} --gtest_filter='
                          'AutomationTest.AutoSaveMultipleFilesTest >{2} 2>{3}'
                          .format(RT_EXE, file_name, log_file_name, err_file_name))
        print 'Point RT command is : ', rt_command
        return rt_command
    elif file_ext == 'ppt':
        if RT_EXE[0] != '/':
            rt_command = ('./{0} {1} --gtest_filter='
                          'AutomationTest.Upsave >{2} 2>{3}'
                          .format(RT_EXE, file_name, log_file_name, err_file_name))
        else:
            rt_command = ('{0} {1} --gtest_filter='
                          '--gtest_filter=AutomationTest.Upsave >{2} 2>{3}'
                          .format(RT_EXE, file_name, log_file_name, err_file_name))
        print 'Point RT command is : ', rt_command
        return rt_command
    else:
        print('Invalid file , Please put files for RT '
              'with .doc,.docx,.xls,.xlsx or .pptx extension')
        move_invalid_file(file_name, dir_list)
        return None


def get_file_extension(file_name):
    '''
    @Description : Extracts file extension from file name
    @param : {String} File name '''
    file_ext = os.path.splitext(file_name)[1][1:]
    return file_ext


def move_rt_file(file_name, dir_list):
    '''
    @Description : Moves roundtrip file & original file to
                   respective directories
    @param : {String} File name'''
    rtfilename = get_rt_file_name(file_name)
    if get_file_extension(file_name) in ('doc', 'docx'):
        if os.path.isfile(INPUT_TEST_FILES_PATH + rtfilename):
            distutils.file_util.move_file(INPUT_TEST_FILES_PATH + rtfilename,
                                          dir_list['round_trip_folder'])
            distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                          dir_list['original_moved'])
    elif get_file_extension(file_name) in ('xls', 'xlsx'):
        distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                      dir_list['original_moved'])
    elif get_file_extension(file_name) in ('ppt'):
        distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                      dir_list['original_moved'])
        print 'roundtripfolderPAth::::::' + dir_list['point_test_data_path'] + file_name + 'x'
        distutils.file_util.move_file('./' + dir_list['point_test_data_path'] + '/' + file_name + 'x',
                                      dir_list['round_trip_folder'])
    else:
        distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                      dir_list['original_moved'])
        print 'roundtripfolderPAth::::::' + dir_list['point_test_data_path'] + file_name
        distutils.file_util.move_file('./' + dir_list['point_test_data_path'] + '/' + file_name,
                                      dir_list['round_trip_folder'])


def get_rt_file_name(file_name):
    '''
    @Description : Generate RT file name
    @param : {String} File name '''
    file_ext = get_file_extension(file_name)
    if file_ext == 'docx':
        rtfilename = 'round_tripped-{0}.docx'.format(file_name)
    elif file_ext == 'doc':
        rtfilename = 'upsaved-{0}.docx'.format(file_name)
    elif file_ext == 'xlsx':
        rtfilename = file_name
    elif file_ext == 'xls':
        rtfilename = file_name
    elif file_ext == 'pptx':
        rtfilename = file_name
    elif file_ext == 'ppt':
        rtfilename = file_name
    return rtfilename


def move_crash_file(file_name, dir_list):
    '''
    @Description : Moves crash file to crash folder
    @param : {String} File name '''
    distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                  dir_list['crash_folder'])


def failed_to_rt(file_name, dir_list):
    '''
    @Description : Moves files to failed_to_rt folder , which could not
                  round trip
    @param : {String} File name '''
    distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                  dir_list['failed_to_rt'])


def move_invalid_file(file_name, dir_list):
    '''
    @Description : Files which are not of word sheet or point
                   Move them to invalid folder
    @param : {String} File name '''
    distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                  dir_list['invalid_folder'])


def move_timeout_file(file_name, dir_list):
    '''
    @Description : Moves file to folder "timeout" which takes more time
    for round tripping than defined time
    @param : {String} File name '''
    distutils.file_util.move_file(INPUT_TEST_FILES_PATH + file_name,
                                  dir_list['timeout'])


def check_if_dir(path):
    '''
    @Description : Check if input path is file or directory before
                   processing it further
    @param : {String} File/Directory name '''
    mode = os.stat(INPUT_TEST_FILES_PATH + path).st_mode
    if stat.S_ISDIR(mode):
        return True
    else:
        return False
