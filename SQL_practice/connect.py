# Testing MySQL connection
# 
# establishes a connection with the MySQL Server using
#
# Usage
# 1. Configure ssh tunnel in seperate shell 
#    `ssh -N -L 8888:127.0.0.1:3306 -i ~/.ssh/STKey.pem bitnami@35.161.173.126`
# 2. `python3 connect.py` 
#

import pymysql

# creates a connection 
conn = pymysql.connect(
    host='127.0.0.1' ,           # localhost is for testing only
    user='USERNAME',             # TODO: username
    password='PASSWORD',         # TODO: password
    db='test', 
    port=8888                    # HTTPS port
     )        

cursor = conn.cursor()           # create cursor

sql = 'SELECT * FROM gps;'       # SQL command: gets 'gps' data from 'test' db

# move cursor to beginning of gps data  
# returns the number rows in gps table
numRows = cursor.execute(sql) 
print("Number of row: ", numRows)

# moves the cursor to the next row in gps data
# returns the data from the current row
data = cursor.fetchone()       
print(data) 
