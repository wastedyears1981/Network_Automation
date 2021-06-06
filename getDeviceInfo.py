import requests
import urllib3
import sys
import json
import DNACconf
import AuthToken

token  = AuthToken.getAuthToken()
user = DNACconf.user
password = DNACconf.password
baseURL = DNACconf.devURL

def getDeviceList():
