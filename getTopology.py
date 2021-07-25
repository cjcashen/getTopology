import requests
import json
from getpass import getpass
from pprint import pprint
from requests.auth import HTTPBasicAuth

USER = input("Please enter your username: ")
PASS = getpass("Please enter your password: ")

BASEURL = 'https://sandboxdnac.cisco.com'
authAPI = "/dna/system/api/v1/auth/token"
deviceTopologyAPI = "/dna/intent/api/v1/topology/physical-topology"

authPayload={}
authHeaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

dnaAuth = BASEURL + authAPI

authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(USER, PASS), headers=authHeaders, data=authPayload)

tokenJSON = authResponse.json()

TOKEN = tokenJSON['Token']

print('Your token was successfully generated. The value of your token is:\n' + TOKEN)


dnaDeviceTopology = BASEURL + deviceTopologyAPI

getPayload={}
getHeaders = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': TOKEN
}

getResponse = requests.get(dnaDeviceTopology, headers=getHeaders, data=getPayload)

getJSON = getResponse.json()

pprint(getJSON)
