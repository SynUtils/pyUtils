#!/usr/bin/python
import os
import subprocess
import csv
import argparse
import timeit


devnull = open(os.devnull, 'w')
def run_asan(binary_file, files_path, parameter):	
	for root, dirs, files in os.walk(files_path):
		for name in files:
			start_time = timeit.default_timer()
			if parameter:
				# exit_code = subprocess.call([binary_file, parameter , (root + '/' + name)], stdout=devnull, stderr=devnull)
				exit_code = subprocess.call([binary_file, parameter , (root + '/' + name)], stdout=devnull, stderr=devnull)

			else:
				# exit_code = subprocess.call([binary_file, (root + '/' + name)], stdout=devnull, stderr=devnull)
				exit_code = os.system('{} {} {}'.format(binary_file, (root + '/' + name), '> /dev/null 2>&1'))
				# exit_code = subprocess.Popen([binary_file , (root + '/' + name)])
				# print "return code",exit_code.returncode
				# print exit_code.wait()

			elapsed = timeit.default_timer() - start_time
			print "{0} {1} {2}".format(root + '/' + name + '  ', os.WEXITSTATUS(exit_code), round(elapsed,2))

			file_name = 'Status_' + str(exit_code) + '.csv'
			#print file_name
			if not os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/' + file_name):
				#print "hi"	
				writer = open(file_name, "wb")
				writer.write('{0}, {1}, {2}'.format('File_name', 'Exit_Code', 'Time Taken'))
				writer.write('\n')
				writer.close()
			writer = open(file_name, "a")
			writer.write('{0}, {1}, {2}'.format(name, os.WEXITSTATUS(exit_code), round(elapsed,2)))
			writer.write('\n')
			writer.close()


if __name__ == '__main__':
	param = ''
	PARSER = argparse.ArgumentParser()

	PARSER.add_argument('-binary_file', default = '/home/synerzip/Documents/asan/asan_point' , help='path of ASAN binary', required=True)
	PARSER.add_argument('-test_files', default = '/home/synerzip/Documents/asan/PointData' , help='Test Files Directory', required=True)
	PARSER.add_argument('-param', default = '', nargs = '?')

	ARGS = PARSER.parse_args()
	if ARGS.param == 'p':
		param = '-p'

	run_asan(ARGS.binary_file, ARGS.test_files, param)
