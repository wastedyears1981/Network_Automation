import requests
import urllib3
import sys
import json
import DNACconf
import AuthToken

token = AuthToken.getAuthToken()
user = DNACconf.user
password = DNACconf.password
baseURL = DNACconf.devURL
auth = DNACconf.auth

payload = {}
headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json',
    'Authorization': auth
}


def getDeviceList():
    url = baseURL + "/dna/intent/api/v1/network-device"
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)


def getInterfaces():
    url = baseURL + "/InterfaceURL" # Needs updating, check CDNAC docs
    response = requests.get(url, headers=headers, data=payload)
    print(response)


