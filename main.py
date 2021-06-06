from getDeviceInfo import *

deviceList = getDeviceList()
x = 0


for device in deviceList:
    x = x + 1
    print(x, ' - ', device['type'],' : ',device['managementIpAddress'])
