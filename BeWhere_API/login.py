# this file contains HTTPS methods for: 
# - authentication: gets a secure token to make requests (2018/08/23)
# - snapshot: get most recent data for ALL beacons (2018/08/23)
# - stream: get data in a specific date range for a specific module (2018/08/27)
# - streamHistory: get data a specific date range for ALL modules (2018/08/27)
#
# usage: `$ python main.py login.py`
#

import requests
import hashlib
import json 

def printResponse(response, response_data):
  print(response.status_code)
  print(json.dumps(response_data, sort_keys=False, indent=4, separators=(',', ': ')))

class Bewhere:
  # NOTE: DO NOT COMMIT WITH CREDENTIALS
  # self.username=<INSERT USERNAME>
  # self.password=<INSERT PASSWORD>  
  # self.account_id=<INSERT ACCOUNT ID> 
  #
  ## sets up the local variables for the username/password
  def __init__(self):
  # self.username=<INSERT USERNAME>
  # self.password=<INSERT PASSWORD>  
  # self.account_id=<INSERT ACCOUNT ID> 
  
  ## authenticates user and adds token to header for future requests
  def login(self):
    url = "https://api.bewhere.com" + "/authentication/" + self.username + "?type=m2m" #type of account = machine to machine (m2m) 
    response = requests.get(url)       # response contains: token and salt
    response_data = response.json()
    # NOTE: DEBUG
    printResponse(response, response_data)
    hashGen = hashlib.sha256()
     
    # Hash our password
    # FIXME: some terminals throwing errors here? 
    hashGen.update(self.password)
    first_hash = hashGen.hexdigest()
 
    # Add it to the salt
    b = bytearray()
    concat = response_data["salt"]+first_hash
    b.extend(concat.encode())
    hashGen_final = hashlib.sha256()
    hashGen_final.update(b)
    final_hash = hashGen_final.hexdigest()
 
    # Post data to send back
    data = {'authphrase' : final_hash,
        'username' : self.username,
        'tidHashAlgorithm' : '2',
        'tidSession' : '3'}
 
    # Set the standard headers to include the token
    self.headers = {'Token': response_data["token"],
    'Accept': 'application/json',
    'Content-Type' : 'application/json'}
 
    url = "https://api.bewhere.com" + "/authentication"
    response = requests.post(url, json=data, headers=self.headers)
    response_data = response.json()
    # NOTE: DEBUG
    printResponse(response, response_data)

## returns the most recent data for all modules
 # add `/{id}` to get the most recent data for a specific module
  def snapshots(self):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/snapshots"
    response = requests.get(url, headers=self.headers)
    response_data = response.json()
    # NOTE: DEBUG
    printResponse(response, response_data)

## returns data in a specific date range for a specific module
  def stream(self):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/streams/" + self.beacon1 + "?start=1535004719000&end=1535062019000"
    response = requests.get(url, headers=self.headers)
    response_data = response.json()
    # NOTE: DEBUG stmt
    printResponse(response, response_data)

## returns data in a specific date range for ALL the modules
  def streamHistory(self):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/streams/history" + "?limit=100&start=1535004719000&end=1535062019000"
    response = requests.get(url, headers=self.headers)
    response_data = response.json()
    # NOTE: DEBUG stmt
    printResponse(response, response_data)
