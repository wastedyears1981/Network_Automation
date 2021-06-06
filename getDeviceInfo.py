import requests
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


# Get list of hardware devices connected to CDNAC
def getDeviceList():
    url = baseURL + "/dna/intent/api/v1/network-device"
    response = requests.get(url, headers=headers, data=payload)
    output = response.json()['response']
    return output


# Get Interface details for device
def getInterfaces(device):
    url = baseURL + "/InterfaceURL"  # Needs updating, check CDNAC docs
    response = requests.get(url, headers=headers, data=payload)


def getDeviceByIp():
    ipInput = input("What IP address would you like to search? ")
    url = baseURL + "/dna/intent/api/v1/network-device/ip-address/{ip}".format(ip=ipInput)
    response = requests.get(url, headers=headers, data=payload)
    output = response.json()['response']
    return output
