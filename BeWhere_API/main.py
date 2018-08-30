from bewhere import *
from demo import * 

def main(): 
  # NOTE: DO NOT COMMIT WITH SENSATIVE DATA -- copy and paste this instead :)
  # username={INSERT USERNAME}
  # password={INSERT PASSWORD}
  # account_id={INSERT ACCOUNT_ID}
  # module ={INSERT MODULE}
  #
  username={INSERT USERNAME}
  password={INSERT PASSWORD}
  account_id={INSERT ACCOUNT_ID}
  module={INSERT MODULE}

  # AUTHENTICATION DEMO 
  ## securely authenticates a user by hashing their password 
  ## connection remains valid as long as the token is valid 
  admin = Bewhere(username, password, account_key)
  admin.login()

  # DATE RANGE DEMO
  ## retrieves points in date range for a given module
  start = parseTime("2018 08 28 08 00 PST")
  end = parseTime("2018 08 28 09 00 PST")
  dateRange(admin, module, start, end)
  
if __name__ == "__main__":
  main()
