from getDeviceInfo import *

deviceList = getDeviceList()


def getDeviceListIP():
    x = 0
    for device in deviceList:
        x = x + 1
        print(x, ' - ', device['type'], ' : ', device['managementIpAddress'])


def searchIP():
    output = getDeviceByIp()
    print(output['type'])


searchIP()