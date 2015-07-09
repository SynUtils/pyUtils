'''
 * Copyright 2013 Google Inc. All Rights Reserved.
 * @fileoverview : RT automation script for
 * word , sheet & point.script contains all
 * functions required to automated roundtrip procedure
 * of word [.doc/.docx] ,Sheet[.xlsx] & point [.pptx] files
 * @author jayashree.patil@synerzip.com (Jayashree Patil)
 * '''
import traceback
import sys
import os
import rt_utils
TIMEOUT = 600

def process_files(test_files, dirs, file_handle):
    '''
    @Description : starts processing files for RT of given input directory
    @param : {List} List of files , {String} input directory name,
             file handle of .csv '''
    for test_file in test_files:
        print "Processing file : ", test_file
        if rt_utils.check_if_dir(test_file) == True:
            print "%s is a directory" % (test_file)
            continue
        file_size_before_rt = rt_utils.get_file_size(
                              rt_utils.INPUT_TEST_FILES_PATH
                              + test_file)
        print "File Size before RT = ", file_size_before_rt
        rt_command = rt_utils.get_rt_command(str(test_file), dirs)
        if rt_command == None:
            continue
        else:
            status, start_time = perform_rt(test_file, dirs, rt_command)
        if status == 0:
            write_rt_process_details(test_file, dirs, file_size_before_rt,
                                     file_handle, start_time)
        elif status == 20:
            rt_utils.failed_to_rt(test_file, dirs)
        elif status == None:
            continue
        else:
            rt_utils.move_crash_file(test_file, dirs)
            print "File :", test_file, " crashed in round trip"
        print "----------------------------------------------"

def perform_rt(test_file, dirs, rt_command):
    '''
    @Description : Perform RT process on given file using rt command
    @param : {String} File name, {String} input directory name,
             {String} rt command '''
    start_time = rt_utils.get_current_time()
    print "Start Time : ", start_time
    status = rt_utils.check_command_status(test_file,
                            rt_command, TIMEOUT,dirs)
    print "---------------RT Command status is : ", status
    return status, start_time


def write_rt_process_details(test_file, dirs, file_size_before_rt,
                            file_handle, start_time):
    '''
    @Description : Writes rt process details to .csv
    @param : {String} File name, {String} input directory name,
             {String} file size before rt , file handle , {Time}
             time when RT process start '''
    row = rt_utils.get_empty_row()
    end_time = rt_utils.get_current_time()
    print "START Time NAGMAIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII: ", start_time
    print "End Time NAGMAIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII: ", end_time
    time_diff = rt_utils.get_time_diff(start_time,
                                       end_time)
    if os.path.exists(
            rt_utils.get_rt_file_path(test_file, dirs)):
        file_size_after_rt = rt_utils.get_file_size(
                rt_utils.get_rt_file_path(test_file, dirs))
        print "File Size after RT = ", file_size_after_rt
        size_diff = (file_size_after_rt -
                     file_size_before_rt)
        #---- assigns value to row dictonary
        row["File Name"] = test_file
        row["O_File_Size"] = file_size_before_rt
        row["R_File_Size"] = file_size_after_rt
        row["File Size Difference After RT"] = size_diff
        row["Time Required"] = time_diff
        row["Start Time"] = str(start_time)
        row["End Time"] = str(end_time)
        rt_utils.write_row(file_handle, row)
        rt_utils.move_rt_file(test_file, dirs)
    else:
        print("There was some error while performing rt"
         " on file : ", test_file)
        rt_utils.failed_to_rt(test_file, dirs)

def main():
    ''' @Description : Initialise rt automation process '''
    try:
        file_handle = None
        file_handle, dirs = rt_utils.init()
        print file_handle
        if file_handle != None:
            rt_utils.write_file_header(file_handle)
            test_files = rt_utils.get_files()
            if test_files != 0:
                process_files(test_files, dirs, file_handle)
        else:
            sys.exit()
    except IOError as err:
        print(err)
        traceback.print_exc()
        sys.exit("Error Occurred")
    finally:
        if file_handle != None:
            file_handle.close()

# Start of execution
if __name__ == '__main__':
    main()
