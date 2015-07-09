'''
Created on 17-Feb-2014

@author: pavang
'''


# if __name__ == '__main__':
#     import httplib2
#     h = httplib2.Http(".cache")
#     resp, content = h.request("http://example.org/", "GET")
#     pass


import json
import httplib2
# from builtins import dir
# 
# print(dir(json))

# print(dir(httplib2))

github_url = 'https://api.github.com/user/repos'

# Get the HTTP object
h = httplib2.Http(".cache") 
h.add_credentials("pvn.gupta.2009@gmail.com", "prabhu_87", "https://api.github.com")
       
           
# Send the GET request
# url = 'http://quickbuild.quickoffice.com:8085/bamboo/rest/api/latest/plan?os_authType=basic'      
(resp_header, content) = h.request(github_url, "GET", headers={'cache-control':'no-cache'})
# jdata = json.loads(content)
print(resp_header)
print(content)

# print(json.loads(content))

