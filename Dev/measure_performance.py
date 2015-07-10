__author__ = 'pavan.gupta@synerzip.com'

import os
import logging
from subprocess import call
import shutil
import subprocess
from synUtil.prop_parser import Properties



# Configuring logger for this module
logger = logging.getLogger(__name__)
handler = logging.FileHandler('/home/synerzip/Documents/pavanWork/tools/performance/performance.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class QoUtil(object):
    """
    This class is for quickoffice utilities which are generic and can be used for other modules also.
    """
    global logger
    #def __init__(self):
    #self.logger = logger
    #logger.info("QU Log")
    #print "QoUtil constructor"

    def count_char(self, char, str) :
        """
        Count the occurrence of a given character in argument str
    Args:
        char: Character for which frequency need to be counted
        str: Source string
    Return:
        Frequency of character
        """
        count = 0
        for ch in str :
            if ch == char :
                count += 1
        return count

    def get_time_format(self, _min, sec, millisec, split_char = ':') :
        """

                Convert given parameters into standard time format(i.e. _min:sec:millisec)
    Args:
        _min: Minutes
        sec: Seconds
        millisec: MilliSeconds
        split_char: separator for time elements
        """
        formated_time = str(_min).rjust(2, '0') + \
                        split_char + str(sec).rjust(2, '0') + \
                        split_char + str(millisec).rjust(3, '0')
        return (formated_time)

    def open_file(self, fileName, mode) :
        """
            a wrapper to open function with exception handling
    Args:
        fileName: Name of file to be opened
        mode: Mode(like r,w,a) in which file will be opened
        """
        try :
            data = open(fileName, mode)
            return data
        except IOError as err :
            logger.exception('File error', str(err))
            data.close()

    def remove_all_files(self, dir_path, rm_dir_tree = False) :
        """
        remove all files in given directory path
        Note: this method will not delete nested directories by default
        """
        if rm_dir_tree == True :
            shutil.rmtree(dir_path)
        else :
            file_list = [f for f in os.listdir(dir_path)]
            for f in file_list :
                file_path = os.path.join(dir_path, f)
                if os.path.isfile(file_path) :
                    os.remove(file_path)

    def write_dict_to_csv(self, _dict, dict_first_key, dict_last_key, file_path) :
        """
        Write a dictionary in csv file
    Args:
        _dict: dictionary which need to be written csv file
        file_path: target csv file which would be generated by this method
        """
        #
        # file_data = p.get_filenames_data(test_files_dir)
        # first_list = qu.list_from_dict_value(p.unmatched_data(file_data['run01.csv'], file_data['run02.csv']), '1')
        # second_list = qu.list_from_dict_value(p.unmatched_data(file_data['run01.csv'], file_data['run02.csv']), '2')
        # qu.remove_keys(first_list,_dict)
        # qu.remove_keys(second_list,_dict)

        with open(file_path, 'w') as f :
            # Below code is to keep <b> File Name </b> key on the top of CSV File
            try :
                f.write(dict_first_key)
                f.write(str(_dict.pop(dict_first_key)))
                f.write('\n')

                lst = list(_dict.keys())
                lst.sort(key = lambda lst: (os.path.splitext(lst)[1],os.path.splitext(lst)[0]))
                #print lst

                for k in lst :
                    if k == dict_last_key :
                        continue
                    f.write(k)
                    f.write(_dict[k])
                    f.write('\n')
                f.write(dict_last_key)
                f.write(str(_dict[dict_last_key]))
            except KeyError as ke :
                logger.exception("Key {0} does not exist in dictionary".format(str(ke)))
                pass
        f.close()

    def execute_py(self, no_of_iteration, csv_generator,
                   source_csv_file_path, csv_generator_args, target_csv_file) :
        """
        Executes python program which invokes c2c tool

        """
        #print "Executing python program"
        #p = subprocess.Popen('python stopWatch.py',shell=True)
        #print p.stdout.read()
        for i in range(no_of_iteration) :
            call(["/usr/bin/python", csv_generator, csv_generator_args, 'BLESSED'])
            #cmd = 'mv -f ' + source_csv_file_path + ' ' + target_csv_file + str(i + 1) + '.csv'
            #os.system(cmd)
            tcsv = target_csv_file + str(i + 1) + '.csv'
            # Calling mv command of unix to move csv file
            call('mv -f {0} {1}'.format(source_csv_file_path, tcsv), shell = True)

    def is_dict_empty(self, dictionary) :
        isempty = (dictionary and True) or False
        return isempty

    def list_from_dict_value(self, dict_data, value) :
        lst = []
        for k, v in dict_data.items() :
            if v == value :
                lst.append(k)
        return lst

    def print_dict(self, dict_data, separator = ':') :
        for key, value in dict_data.items() :
            print key + separator + '   ' + value

    def remove_keys(self, lst, dictionary):
        for l in lst:
            dictionary.pop(l,None)


class Performance :
    """
     This class contains function which be helpful in measuring the performance of all quickoffice
     applications(i.e. word/sheet/point)
    """
    logger = None
    pdata = {}
    pdata_first_key = 'File Name'
    pdata_last_key = 'Total Load Time Of Iterations :'

    total_load_time_of_iterations = ''
    csv_file_count = 0
    qu = QoUtil()

    def __init__(self, logger, test_files_dir, target_csv_file) :
        """
            initializing Performance class variables
        """
        self.logger = logger
        self.test_files_dir = test_files_dir
        self.target_performance_csv_file = target_csv_file
        #print "Inside Performance Constructor"

    def remove_non_csv_files(self, test_files_dir_path) :
        """
        this method will delete files other then csv
    Args:
    test_files_dir_path: test files source directory path
        """
        file_list = os.listdir(test_files_dir_path)
        for f in file_list :
            if not f.endswith('.csv') :
                try :
                    os.remove(test_files_dir_path + '/' + f)
                except OSError, e :
                    logger.exception("Error in %s : %s" % (e.filename, e.strerror))

    def convert_time_format(self, time_part) :
        """
        this method convert time format from <b> min-sec.millisec </b> to <b> min:sec:millisec </b>
    Args:
        time_part:
        """

        try :
            minute_time_part = str(time_part.split('-')[0]).replace('\n','').rjust(2, '0')
            if not '-' in time_part:
                seconds_time_part = '00'
            else:
                seconds_time_part = (str(time_part.split('-')[1]).split('.')[0]).replace('\n','').rjust(2, '0')

            if not '.' in time_part:
                millisec_time_part = '000'
            else:
                millisec_time_part = (((str(time_part.split('-')[1])
                                    .split('.')[1])[:3]).replace('\n', '')).ljust(3, '0')
        except BaseException as ex :
            logger.exception('Incorrect input format for time_part: ' + str(ex.message))
            return -1

        return '{0}:{1}:{2}'.format(minute_time_part,
                                    seconds_time_part,
                                    millisec_time_part)

    def add_time_list(self, time_list, list_split_char = ' ', time_split_char = ':') :
        """
          generates total of time list
    Args:
        time_list: list of elements(each representing time in _min:sec:Millisecond) format
        list_split_char: separator for list items
        time_split_char: separator for each part(which is representing time like _min,sec, millisec)
        of item
    Return:
        Total of all list items
        """
        total_min = 0
        total_second = 0
        total_millisec = 0

        #print time_list

        scrutinized_list = (str(time_list).replace(',', "").strip()).split(list_split_char)
        for line in scrutinized_list :
            try :
                _min, sec, millisec = line.replace(',', '').strip().split(time_split_char)
                total_min += int(_min)
                total_second += int(sec)
                total_millisec += int(millisec)
            except ValueError as ve :
                logger.exception('{0} need more than 1 value to unpack'.format(line))
                pass

            #print min +":"+ sec +":"+ millisec

        total_second += (total_millisec / 1000)
        total_min += (total_second / 60)

        #total_time = str(total_min).rjust(2, '0') + ":" + str(total_second % 60).rjust(2, '0') \
        #             + ":" + str(total_millisec % 1000)
        total_time = qu.get_time_format(total_min, str(total_second % 60),
                                        str(total_millisec % 1000))

        return total_time

    def calc_avg_time(self, total_time, no_of_files, time_split_char = ':') :
        """
        calculate average time for no of files
    Args:
    total_time: single time instance(like _min:sec:millisec) which is total of time taken
        by one file in all iterations
    no_of_files: dividing factor for average calculation of time

        """
        _min, sec, millisec = str(total_time).strip().split(time_split_char)
        total_millisec = int(millisec) + (int(sec) * 1000) + (int(_min) * 60 * 1000)
        # Mean time in milliseconds

        try :
            mean_time = total_millisec / no_of_files
            hour = mean_time / (60 * 60 * 1000)
            mean_time = mean_time % (60 * 60 * 1000)
            _min = mean_time / (60 * 1000)
            mean_time = mean_time % (60 * 1000)
            sec = mean_time / (1000)
            mean_time = mean_time % 1000
            millisec = mean_time

            #print _min + ':' + sec + ':' + millisec
            return str(hour).rjust(2, '0') + ':' + str(_min).rjust(2, '0') + ':' + \
                    str(sec).rjust(2, '0') + '.' + str(millisec).rjust(3, '0')

            #return self.qu.get_time_format(_min, sec, millisec)
        except ZeroDivisionError as ex :
            logger.exception('No of files is zero: %s' + str(ex))
            return

    def add_csv_file(self, file, mode) :
        """
        analyze one csv file and add it to dictionary
    Args:
        file: csv file to be analyzed
        mode: file opening mode like r,w,a.
        """

        f = None
        totalLoadTime = 0
        totalTimeInSecond = 0.0
        try :
            f = self.qu.open_file(file, mode)
            try :
                for line in f :
                    timePart = line.rpartition(':')[2]
                    firstPart = line.split(':', 2)[0]

                    #print self.convert_time_format(timePart)
                    if firstPart not in self.pdata :
                        self.pdata[firstPart] = ', ' + str(self.convert_time_format(timePart))
                    else :
                        self.pdata[firstPart] += ', ' + str(self.convert_time_format(timePart))

                    totalLoadTime += int(timePart.split('-')[0])
                    totalTimeInSecond += float(timePart.split('-')[1])
            except ValueError as ex :
                logger.exception("Incompatible number format: " + str(ex))
            f.close()
        except IOError as ex :
            logger.exception("File can not be opened" + str(ex))
            f.close()
            pass

        totalLoadTime += int(totalTimeInSecond / 60)
        totalLoadTime = str(totalLoadTime) + '-' + (str(totalTimeInSecond % 60)[:6])
        self.total_load_time_of_iterations += ', ' + self.convert_time_format(str(totalLoadTime))

    def get_last_column_to_string(self, element_separator = ' ') :
        """
        returns last column of dictionary as string, separated by space
    Args:
    element_separator: Element separator used in concatenated string
    return: concatenated string(element separator) constructed by last column

        """
        ttstr = ''
        # calculating vertical total time
        for k in self.pdata :
            # below condition will skipp additional keys(File Name and Total Load Time Of Iterations)
            if k == self.pdata_first_key or k == self.pdata_last_key :
                continue
            ttstr = ttstr + (str(self.pdata[k]))[str(self.pdata[k]).rfind(element_separator) :]
        return ttstr

    def fill_dict(self) :
        """
            filling dictionary with required data, which is required to put in CSV
        """

        # filling file names in dictionary and additional value for total and average time
        if os.path.isdir(self.test_files_dir) :
            flist = os.listdir(self.test_files_dir)
            self.pdata[self.pdata_first_key] = str(flist).replace("'", '')

            #self.pdata[self.pdata_first_key] = ', ' + (self.pdata[self.pdata_first_key])[1 :-1] + \
            #                                   ', Total Time, Average Time '
            self.pdata[self.pdata_first_key] = ', ' + (self.pdata[self.pdata_first_key])[1 :-1] + \
                                               ', Average Time '

            for l in flist :
                self.add_csv_file(self.test_files_dir + '/' + l, 'r')
                self.csv_file_count += 1

            # adding total time to dictionary
            total_time = ''
            for k in self.pdata :
                #skipping additional key(File Name and Total Load Time Of Iterations)
                if k == self.pdata_first_key or k == self.pdata_last_key :
                    continue
                total_time += self.add_time_list(self.pdata[k]) + ' '
                #self.pdata[k] += ', ' + self.add_time_list(self.pdata[k])

            # adding Average Time to dictionary
            # below line is commented because removing Total Time column from dictionary
            #last_column = self.get_last_column_to_string().strip().split(' ')
            bkp_last_column = total_time.strip().split(' ')
            lst_count = 0
            for k in self.pdata :
                if k == self.pdata_first_key :
                    continue
                # below line is commented because removing Total Time column from dictionary
                #self.pdata[k] += ', ' + self.calc_avg_time(last_column[lst_count],
                #                                           self.csv_file_count)
                self.pdata[k] += ', ' + self.calc_avg_time(bkp_last_column[lst_count],
                                                           self.csv_file_count)
                lst_count += 1

            # adding Total time of iterations to dictionary
            # Please do not move below line on top of above for loop that will scrud the calculations
            # of <b> Total Time </b> and <b> Average Time </b> Column
            self.pdata[self.pdata_last_key] = self.total_load_time_of_iterations
            grand_total = self.add_time_list(self.pdata[self.pdata_last_key])

            #self.pdata[self.pdata_last_key] += ', ' + self.add_time_list(
            #    self.pdata[self.pdata_last_key])
            #grand_total = (str(self.pdata[self.pdata_last_key]))[str(
            #    self.pdata[self.pdata_last_key]).rfind(' ') :]
            self.pdata[self.pdata_last_key] +=  ', ' + self.calc_avg_time(grand_total, self.csv_file_count)
        else :
            pass

    def validate_pdata(self, expected_columns) :
        #d={'1':'1,2,3,4,5', '2':'f,d,g,h', '3':'d,fg,d,fg,dfg,d'}
        for k in self.pdata :
            if not expected_columns == qu.count_char(',', self.pdata[k]) :
                logger.error(k + ' is missing in one of the csv')
                #self.pdata.pop(k)

    def validate_total(self) :
        """
        Validate horizontal and vertical total of dictionary
        """
        ttstr = ''
        # calculating vertical total time of dictionary items
        for k in self.pdata :
            # below condition will skipp additional keys(File Name and Total Load Time Of Iterations)
            if k == self.pdata_first_key or k == self.pdata_last_key :
                continue
            ttstr = ttstr + (str(p.pdata[k]))[str(p.pdata[k]).rfind(' ') :]

        # Calculating horizontal total time of dictionary items
        logger.info('Vertical Total: ' + self.add_time_list(ttstr))
        logger.info('Horizontal Total: ' + self.add_time_list(self.pdata[self.pdata_last_key]))

    def validate_files(self, char = ',') :
        """
        validate data of file on the basis of separator char
    Args:
        char:
        """
        file_count = os.listdir(self.test_files_dir)
        logger.info(len(file_count))
        for k in self.pdata :
            if len(file_count) != self.qu.count_char(char, self.pdata[k]) :
                logger.info("entry is missing for: {0} in any of the csv file".format(str(k)))

                #print "validated"

                #if len(file_count) ==

    def validate_file_lines_with_dict(self) :
        print "validated"

    def print_dict(self) :
        """
        print dictionary elements on console
        """
        print (self.pdata_first_key + '\t' * 3).ljust(63) + str(self.pdata[self.pdata_first_key])
        i = 1
        for k in self.pdata :
            if k == self.pdata_first_key or k == self.pdata_last_key :
                continue
            print str(i) + '  ' + str(k).ljust(64) + '\t\t' + str(self.pdata[k]).replace('\n', ',\t\t\t\t')
            i += 1
            #self.pdata[self.pdata_last_key] = ', ' + (str(self.total_load_time_of_iterations)
        #                                               [1:-1]).replace("'", '')


        print self.pdata_last_key + '\t' * 10 + \
              self.pdata[self.pdata_last_key] + '\t'
        print '*' * 140

    def get_filenames_data(self,test_files_dir):
        lst = os.listdir(test_files_dir)
        lst.sort()
        flist_data = {}
        for f in lst :
            flist = subprocess.check_output(['cut', '-d', ':', '-f', '1', test_files_dir + '/' + f])
            flist_data[f] = flist.split('\n')

        return flist_data

    def unmatched_data(self, first_list, second_list):
        unmached = {}
        for f in first_list :
            if f not in second_list :
                unmached[f] = '1'

        for f in second_list :
            if f not in first_list :
                unmached[f] = '2'

        return unmached


if __name__ == '__main__' :
    base_dir = r'/home/synerzip/Projects/loadPerformance/master/'
    #base_dir = r'/home/synerzip/Projects/loadPerformance/master/'


    #Performance
    test_files_dir = base_dir + 'src_csv_files'
    target_performance_csv_file = base_dir + 'master_performance.csv'

    #QoUtil
    log_file_path = base_dir + 'performance.log'
    no_of_iteration = 1
    csv_generator = '/home/synerzip/Projects/loadPerformance/html-office/crx/e2eTests/c2cTests/report/generate_report.py'
    csv_generator_args = base_dir + 'c2cprop.txt'
    source_csv_file_path = '/home/synerzip/Projects/loadPerformance/html-office/crx/e2eTests/c2cTests/report/profileData.csv'
    target_csv_file = base_dir + 'src_csv_files/run0'

    #config_logger(log_file_path)

    p = Performance(logger, test_files_dir, target_performance_csv_file)
    qu = QoUtil()

    print '***' * 80
    logger.info('***' * 80)
    logger.info('Clearing test csv file directory')
    qu.remove_all_files(test_files_dir)
    qu.execute_py(no_of_iteration, csv_generator, source_csv_file_path, csv_generator_args, target_csv_file)
    print "CSV files created"
    logger.info('CSV files created')


    # # CSV File Processing
    print "Deleting Non CSV files"
    logger.info('Deleting Non CSV files from test files directory...')

    p.remove_non_csv_files(test_files_dir)

    print "Non CSV Files Deleted"
    logger.info('Non CSV Files Deleted')

    print "Filling data in Dictionary"
    logger.info('Filling data in Dictionary')
    p.fill_dict()

    print "Data Filled in the Dictionary"
    logger.info('Data Filled in the Dictionary')

    logger.info('Validating dictionary data')

    p.validate_pdata(no_of_iteration + 1)

    p.print_dict()
    print "Performance data written in: " + target_performance_csv_file
    qu.write_dict_to_csv(p.pdata, p.pdata_first_key, p.pdata_last_key, p.target_performance_csv_file)

    print "**********************     Done     **************************"

    # file_data = p.get_filenames_data(test_files_dir)
    #
    # print(qu.list_from_dict_value(p.unmatched_data(file_data['run01.csv'], file_data['run02.csv']), '1'))
    # print(qu.list_from_dict_value(p.unmatched_data(file_data['run01.csv'], file_data['run02.csv']), '2'))

    #
    #print p.convert_time_format('34-2.24')
    #print p.convert_time_format('0-1')
    #print p.convert_time_format('5')
    #qu.remove_all_files(test_files_dir)

    #p.remove_non_csv_files('/Users/pavang/Documents/testSample')

    #print p.get_last_column_to_string()
    #print p.pdata
    #print p.calc_avg_time('10:50:500', 2)
    #p.validate_total()
    #for k in p.pdata:
    #    print p.add_time_list(p.pdata[k])

    #qo = QoUtil()
    #qo.execute_py()
    #p.validate_files()
    #print p.file_count
    #print len(p.pdata.keys())

