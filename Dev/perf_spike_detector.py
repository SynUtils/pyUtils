from mongoengine import *


prev_build = []
current_build = []


# def read_mongodb(document_name):
# 	connect('perf')
#     for dn in document_name.objects:
# 	    print('*=' * 40)
# 	    for k, v in dn.build_data.items():
# 	        print (k,v)
# 	    # print dn.build_data
# 	print('*=' * 40)


def read_csv(prev_build_file, current_build_file):
	global prev_build, current_build
	with open(prev_build_file) as prev_file, open(current_build_file) as cur_file:
		for p_line, c_line in zip(prev_file, cur_file):
			prev_build.append(p_line)
			current_build.append(c_line)



def spike_detector(prev_build, current_build, output_file, spike_indecator_per = 10):
	with open(output_file, 'w') as of:
		for prev, current in zip(prev_build, current_build):
			is_spike = False
			prev_hours, prev_minutes, prev_seconds =  prev.strip().split(':')
			prev_seconds, prev_miliseconds = prev_seconds.split('.')
			total_prev_miliseconds = (int(prev_hours) * 60 * 60 * 1000) + (int(prev_minutes) * 60 * 1000) + (int(prev_seconds) * 1000) + int(prev_miliseconds)
			# print total_prev_miliseconds
			# print total_prev_miliseconds * spike_indecator_per / 100


			current_hours, current_minutes, current_seconds =  current.strip().split(':')
			current_seconds, current_miliseconds = current_seconds.split('.')
			total_current_miliseconds = (int(current_hours) * 60 * 60 * 1000) + (int(current_minutes) * 60 * 1000) + (int(current_seconds) * 1000) + int(current_miliseconds)
			# print total_current_miliseconds
			if (total_current_miliseconds - total_prev_miliseconds) >=  (total_prev_miliseconds * spike_indecator_per / 100):
				is_spike = True

			# of.write("{0} \t {1} \t {2} \t {3} \n".format(prev, current, float(((total_current_miliseconds - total_prev_miliseconds) * 100) / total_prev_miliseconds), is_spike))

			csv_str = str(prev)[:-1] + ', ' + str(current)[:-1] + ', ' + str(float(((total_current_miliseconds - total_prev_miliseconds) * 100) / total_prev_miliseconds)) + ', ' + str(is_spike)
			# of.write(prev)
			# of.write(current)
			# of.write(str(float(((total_current_miliseconds - total_prev_miliseconds) * 100) / total_prev_miliseconds)))
			# of.write(str(is_spike))
			of.write(csv_str)
			of.write('\n')

			print "{0}     {1}    {2}     {3}".format(prev, current, float(((total_current_miliseconds - total_prev_miliseconds) * 100) / total_prev_miliseconds), is_spike)

		# print is_spike

if __name__ == '__main__':
	p_file = '/tmp/866_avgOpenPerformance.txt'
	c_file = '/tmp/873_avgOpenPerformance.txt'
	output_file = '/tmp/spike_detector.csv'

	read_csv(p_file, c_file)
	spike_detector(prev_build, current_build, output_file, 10)



