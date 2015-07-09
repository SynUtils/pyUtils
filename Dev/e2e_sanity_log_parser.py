'''
Created on Sep 16, 2014

@author: pavang
'''
import os
import csv

def read_log(input_file_path, output_file_path):    
    with open(output_file_path,'w') as csv_file:
        spec_result = ''
        _file = ''
        suite = ''
        spec = ''
        failed_text = ''
        csv_writer = csv.writer(csv_file, delimiter = ',')
        csv_writer.writerow(['suite', 'spec', 'file', 'Error', 'spec_result'])         
        if os.path.isfile(input_file_path):            
            for line in open(input_file_path).readlines():
                line = str(line)
                final_text = line[line.find(':') + 1 :]
                if line.find('Spec result:') >= 0:
                    spec_result = final_text[:final_text.find('[')]
                if line.find('File:') >= 0:
                    _file = final_text
                if line.find('Suite:') >= 0:
                    suite = final_text
                if line.find('Spec:') >= 0:
                    spec = final_text 
                if line.find('Assertion 1') >= 0:
                    failed_text = final_text
                print(line) 
                if spec_result and _file and suite and spec:
                    if spec_result.find('failed') >= 0 and failed_text == '':
                        continue                                        
                    csv_writer.writerow([suite, spec, _file,  failed_text, spec_result])
                    spec_result = _file = suite = spec= failed_text= ''

def read_csv(input_file):
    row_dict = { "id": "0", "title": "Pavan", "totaldefect": "HelloMrDJ" }
    with open(input_file) as csv_file:
        file_data = csv.reader(csv_file)
        for row in file_data:            
            print(row)

if __name__ == '__main__':
    input_file_path = r'/tmp/pavan.log'
    output_file_path = r'/tmp/e2e.csv'
#     read_log(input_file_path, output_file_path)
    read_csv(output_file_path)
    pass



