# this file contains HTTPS methods for: 
# - login: gets a secure token to make requests (2018/08/23)
# - snapshots: get most recent data for ALL beacons (2018/08/23)
# - stream: get data in a specific date range for a specific module (2018/08/27)
# - streamHistory: get data a specific date range for ALL modules (2018/08/27)
#
# usage: `$ make`
#

import requests
import hashlib
import json 

def printResponse(response):
  print(response.status_code)
  response_data = response.json()
  print(json.dumps(response_data, sort_keys=True, indent=4, separators=(',', ': ')))

class Bewhere:
  # sets up the local variables for the username/password
  def __init__(self, username, password, account_key):
    self.username=username
    self.password=password
    self.account_key=account_key 

  ## AUTHENTICATION 
  def login(self):
    url = "https://api.bewhere.com" + "/authentication/" + self.username + "?type=m2m" #type of account = machine to machine (m2m) 
    response = requests.get(url)       # contains: token and salt
    response_data = response.json()
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
    return response

  ##ACCOUNTS
  # returns list of all accounts with details
  def get_accounts(self):
    url = "https://api.bewhere.com" +"/accounts/" + self.account_key + "/users"
    response = requests.get(url, headers=self.headers)
    return response

  # returns single account with details
  def get_account(self):
    url = "https://api.bewhere.com" +"/accounts/" + self.account_key + "/users/" + self.username
    response = requests.get(url, headers=self.headers)
    return response

  ##OTHER
  # returns the most recent data for all modules
  # TODO: snapshots -- add `/{id}` to get the most recent data for a specific module
  def snapshots(self):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/snapshots"
    response = requests.get(url, headers=self.headers)
    return response

  # returns data in a specific date range for a specific module
  def stream(self, module, startTime, endTime):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/streams/" + module + "?start=%d&end=%d" % (startTime, endTime)
    response = requests.get(url, headers=self.headers)
    return response

  # returns data in a specific date range for ALL the modules
  def streamHistory(self):
    url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/streams/history" + "?limit=100&start=1535004719000&end=1535062019000"
    response = requests.get(url, headers=self.headers)
    return response
