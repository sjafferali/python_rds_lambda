from __future__ import print_function
import sys
import logging
import pymysql
import json

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)
print('Loading function')

#rds settings
rds_host  = "my_db_host_name"
name = "someDBUsername"
password = "somePassword"
db_name = "whm"
port = 3306

def lambda_handler(event, context):
	# Get the object from the event and show its content type
	try:
		conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
	except:
		print('ERROR: Could not connect to MySql instance.')
		sys.exit()
	
	item_count = 0
	response = ""
	try:
		with conn.cursor() as cur:
			cur.execute("show tables")
			for row in cur:
				item_count += 1
				response = response + row[0] + ", "
				print(row[0])

	except:
		print('UnCaught Error')

	finally:
		conn.close()

	return response