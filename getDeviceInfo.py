import requests
import urllib3
import sys
import json
import DNACconf
import AuthToken
import pprint

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

# Get list of hardware devices connected to CDNAC
def getDeviceList():
    url = baseURL + "/dna/intent/api/v1/network-device"
    response = requests.get(url, headers=headers, data=payload)
    output = response.json()['response']
    return output

# Get Interface details for device
def getInterfaces(device):
    url = baseURL + "/InterfaceURL" # Needs updating, check CDNAC docs
    response = requests.get(url, headers=headers, data=payload)


