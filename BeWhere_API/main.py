from bewhere import *
from demo import * 

def main(): 
  # NOTE: DO NOT COMMIT WITH SENSATIVE DATA -- copy and paste this instead :)
  # username={"INSERT_USERNAME"}
  # password={"INSERT_PASSWORD"}
  # account_key={"INSERT_ACCOUNT_ID"}
  # module={"INSERT_MODULE"}
  username={"INSERT_USERNAME"}
  password={"INSERT_PASSWORD"}
  account_key={"INSERT_ACCOUNT_ID"}
  module={"INSERT_MODULE"}
  start = parseTime("2018 08 28 08 00 PST")
  end = parseTime("2018 08 28 09 00 PST")

  ## AUTHENTICATION DEMO 
  # securely authenticates a user by hashing their password 
  # connection remains valid as long as the token is valid 
  user = Bewhere(username, password, accountId)
  printResponse(user.login())


  ## ACCOUNTS DEMO
  # if user has the ADMINISTRATOR role
  # returns list of all users with details
  printResponse(user.get_accounts())
  # returns single user with details
  printResponse(user.get_account())


  ## DATE RANGE DEMO
  # retrieves points in date range for a given module
  dateRange(user, module, start, end)
  
if __name__ == "__main__":
  main()
