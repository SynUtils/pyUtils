'''
Created on 01-May-2014

@author: pavang
'''
import gdata.projecthosting.client
import gdata.projecthosting.data
import gdata.gauth
import gdata.client
import gdata.data
import atom.http_core
import atom.core

def GetAuthSubUrl():
  next = 'https://www.coolissuetrackingsite.com/welcome.pyc'
  scope = 'https://code.google.com/p/chromium/issues'
  secure = True
  session = True
  return gdata.gauth.generate_auth_sub_url.GenerateAuthSubURL(next, scope, secure, session);

authSubUrl = GetAuthSubUrl();
print '<a href="%s">Login to your Google account</a>' % authSubUrl    
    