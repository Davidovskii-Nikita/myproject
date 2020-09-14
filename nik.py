import requests
import psycopg2
import time
import datetime
import json
from psycopg2 import sql

conn = psycopg2.connect(dbname='myproject',
						user='myprojectuser',
						password='password',
						host='localhost')
cur = conn.cursor()


while 1:
	time.sleep(1)
	response = requests.get('http://192.168.43.121')
	k=json.loads(response.text)
	print(k['t1'])
	tim = datetime.datetime.today()
	cur.execute(
				'INSERT INTO main_temperatura ("Number","Value","Time") VALUES (%s, %s, %s)',(1,k['t1'],tim)
				)
	conn.commit()
	cur.execute(
				'INSERT INTO main_temperatura ("Number","Value","Time") VALUES (%s, %s, %s)',(2,k['t2'],tim)
				)
	conn.commit()
	cur.execute(
				'INSERT INTO main_davlenie ("Number","Value","Time") VALUES (%s, %s, %s)',(1,k['p1'],tim)
				)
	conn.commit()
	cur.execute(
				'INSERT INTO main_davlenie ("Number","Value","Time") VALUES (%s, %s, %s)',(2,k['p2'],tim)
				)
	conn.commit()


	# w=len(k)
	# print('Nach dlinna:',len(k))
	# o=1
	# while w!=0:
	# 	print('schet2',o)
	# 	o=o+1
	# 	if k[0]=='t':
	# 		number_t=k[1]
	# 		k=k[3:]
	# 		val_t=k[0:k.find(' ')]
	# 		k=k[k.find(' ')+1:]
	# 		tim = datetime.datetime.today()
	# 		cur.execute(
	# 					'INSERT INTO main_temperatura ("Number","Value","Time") VALUES (%s, %s, %s)',(number_t,val_t,tim)
	# 					)
	# 		conn.commit()
	# 	elif k[0]=='d':
	# 		number_d=k[1]
	# 		k=k[3:]
	# 		val_d=k[0:k.find(' ')]
	# 		k=k[k.find(' ')+1:]
	# 		cur.execute(
	# 					'INSERT INTO main_davlenie ("Number","Value","Time") VALUES (%s, %s, %s)',(number_t,val_t,tim)
	# 					)
	# 		conn.commit()
	# 	else:
	# 		k=''
	# 	w=len(k)
conn.close()
