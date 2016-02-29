'''
Created on Nov 3, 2014

@author: pavang
'''
import cgi
import urllib2
# import urllib.request 




def get_header():
    URL1 = r"http://www.academia.edu/9058809/PROJ_586_Week_8_Final_Exam_Version_1_.docx"
    URL2 = r"https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&ved=0CCkQFjAC&url=http%3A%2F%2Fwww.housinganywhere.com%2FLease_contract_English.docx&ei=FoJXVO_zI46suQTq_ILIAQ&usg=AFQjCNHgUMwb_EW99opYX0tmQG9Ee1cxkA&sig2=-MbYSV5ib9JjhAUIFZ1Nyw&bvm=bv.78677474,d.c2E&cad=rja"
    response = urllib2.urlopen(URL1)
#     response = urllib3.response(URL)
    print response.headers
    first_part, params = cgi.parse_header(response.headers.get('Content-Disposition', ''))
#     filename = params['filename']
    print '-' * 70
    print first_part, params
    
    

if __name__ == '__main__':
    get_header()
    pass