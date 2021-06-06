import requests
import urllib3
import DNACconf
import json

urllib3.disable_warnings()
baseURL = DNACconf.devURL
payload = {}
headers = {
    'Authorization': DNACconf.auth
}


def getAuthToken():
    url = baseURL + "/dna/system/api/v1/auth/token"
    response = requests.post(url, headers=headers, data=payload)
    output = response.json()
    return output['Token']
