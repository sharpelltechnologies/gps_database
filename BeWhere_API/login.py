# this file contains HTTPS functions for: 
# - authentication: get a secure token to make requests
# - snapshot: get a snapshot of the current beacons
# - TODO: accounts: get a list of accounts
# - TODO: streams/history how are these different than snapshots? 

import requests
import hashlib
import json 

class Bewhere:
  ## Sets up the local variables for the username/password
  # NOTE: DO NOT COMMIT WITH CREDENTIALS
  #
  # self.username=<INSERT USERNAME>
  # self.password=<INSERT PASSWORD>  
  # self.account_id=<INSERT ACCOUNT ID> 
  def __init__(self):
    self.username=<INSERT USERNAME>
    self.password=<INSERT PASSWORD>  
    self.account_id=<INSERT ACCOUNT ID> 

  def login(self):
    url = "https://api.bewhere.com" + "/authentication/" + self.username + "?type=m2m" #type of account = machine to machine (m2m) 

    response = requests.get(url)       # response contains: token and salt
    response_data = response.json()
    # NOTE: DEBUG
    print(response.status_code)
    print json.dumps(response_data, sort_keys=False, indent=4, separators=(',', ': '))
    hashGen = hashlib.sha256()
     
    # Hash our password
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
 
    post_url = "https://api.bewhere.com" + "/authentication"
    response = requests.post(post_url, json=data, headers=self.headers)
    response_data = response.json()
    # NOTE: DEBUG
    print(response.status_code)
    print json.dumps(response_data, sort_keys=False, indent=4, separators=(',', ': '))

  def snapshots(self):
    poll_url = "https://api.bewhere.com" + "/accounts/" + self.account_key + "/snapshots"
    snapshot = requests.get(poll_url, headers=self.headers)
    response_data = snapshot.json()
    # NOTE: DEBUG
    print(snapshot.status_code)
    print json.dumps(response_data, sort_keys=False, indent=4, separators=(',', ': '))
