# cisco asa rest-api test
# found known bug with request headers requiring user-agent:
# https://quickview.cloudapps.cisco.com/quickview/bug/CSCvp32185

import json
import urllib3
import requests
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

asaUser = 'nope'
asaPass = 'nope'
host = 'A.B.C.D'
port = '443'

url = f"https://{host}:{port}/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"

headers = {
    "User-Agent": "REST API Agent",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

restApiResponse = requests.get(url, headers=headers, auth = (asaUser, asaPass), verify=False).json()

# Debug full json output
#pprint(json.dumps(restApiResponse, indent=2, sort_keys=True))

asaNameif = restApiResponse["name"]
asaInterfaceIpType = restApiResponse["ipAddress"]["kind"]
asaInterfaceIpAddress = restApiResponse["ipAddress"]["ip"]["value"]
asaInterfaceNetMask = restApiResponse["ipAddress"]["netMask"]["value"]

concatResult = f"Interface: {asaNameif}\nIP Type: {asaInterfaceIpType}\nIP Address: {asaInterfaceIpAddress}\nSubnet Mask: {asaInterfaceNetMask}"

print(concatResult)