import requests
import urllib3
import DNACconf

urllib3.disable_warnings()
baseURL = DNACconf.devURL
url = baseURL + "/dna/system/api/v1/auth/token"
payload={}
headers = {
  'Authorization': DNACconf.auth
}


def getAuthToken():
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)