'''
Created on 07-Oct-2013

@author: pavang
'''
import io
import os

# parse parameters passed to Rake
def parse_params
  ENV['QOCPP_BUILD_ROOT_DIR']=File.dirname(__FILE__)+"/../../../"
  ENV['PYTHONPATH']=File.dirname(__FILE__)
  fail "\n=====ERROR: PARAMS not passed to Rake command.\n" if ENV['PARAMS'].nil?
  params = ENV['PARAMS'].split(',').collect { |val| val.downcase.strip }
#   puts(params)
  intersection = ALL_TARGETS & params
  ENV["QO_BUILD_PLATFORM"] = (intersection.size == 1) ? intersection.first : nil
  intersection = BIT_SIZES & params
  ENV["QO_BUILD_BITSIZE"] = (intersection.size == 1) ? intersection.first : nil
  # pnacl has no bit size, so...
  ENV["QO_BUILD_BITSIZE"] = "" if TARGETS_THAT_IGNORE_BITSIZE.include?(ENV["QO_BUILD_PLATFORM"])
  fail "\n=====ERROR: Insufficient / Unrecognized parameters\n" unless ENV["QO_BUILD_BITSIZE"] and ENV["QO_BUILD_PLATFORM"]
end

def parse_params():
    print("Hello From Python")
    os.environ['QOCPP_BUILD_ROOT_DIR'] = os.path.dir_name(__FILE__) + "/../../../"
    os.environ["PYTHONPATH"] = os.path.dir_name(__FILE__)
    if(os.environ['PARAMS'] == None):
        print("=====ERROR: PARAMS not passed to Rake command.")
        exit()
    else
        params = os.environ['PARAMS'].split(',')
        





if __name__ == '__main__':
    parse_params()