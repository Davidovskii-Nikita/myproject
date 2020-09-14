import requests
import psycopg2
import time
import datetime
from psycopg2 import sql

conn = psycopg2.connect(dbname='myproject',
						user='myprojectuser',
						password='password',
						host='localhost')
cur = conn.cursor()
#print(psycopg2.__libpq_version__)
#cur.execute('''CREATE TABLE STUDENT  
#	(ADMISSION INT PRIMARY KEY NOT NULL,
#	NAME TEXT NOT NULL,
#	AGE INT NOT NULL,
#	COURSE CHAR(50),
#	DEPARTMENT CHAR(50));''')
#conn.commit()
#cur.execute(
#	"INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (13,'jkhu',13,'asd','asd')"
#	)
#conn.commit()
k='t1 268.9898 d3 354.02 t2 354.97 d6 235.98 t1 5687.36'
#t='1 2 456'
while 1:
	l=1
	#print(l)
	l=l+1
	#response = requests.get('http://192.168.43.121')
	#a=response.text
	lengs=len(k)
	start=0
	w=len(k)
	print('Nach dlinna:',len(k))
	while w!=0:
		if k[0]=='t':
			number_t=k[1]
			k=k[3:]
			val_t=k[0:k.find(' ')]
			k=k[k.find(' ')+1:]
			print('number_t: ',number_t, ' val_t: ', val_t)
			time.sleep(2)
		elif k[0]=='d':
			number_d=k[1]
			k=k[3:]
			val_d=k[0:k.find(' ')]
			k=k[k.find(' ')+1:]
			print('number_d: ',number_d, ' val_d: ', val_d)
			time.sleep(2)
		else:
			k=''
		w=len(k)
		print('kon dkinna: ',len(k))
		print('Final k:',k)
		time.sleep(1)
		
	number_t=k[k.find('t')+1]
	#print('number_t:', number_t,)
	k=k[k.find('t')+3:]

	#if k[0]=='1':
	#	num_tem=int(k[2])
	#	#print('val: ',num_tem, 'type:',type(num_tem))
	#	val_tem=float(k[4:])
	#	tim = datetime.datetime.today()
	#	cur.execute(
	#				'INSERT INTO main_temperatura ("Number","Value","Time") VALUES (%s, %s, %s)',(num_tem,val_tem,tim)
	#				)
	#	conn.commit()
	#print('Nomer = '+num_tem+' Velich = '+val_tem)
	#print(a)
	time.sleep(10)
#conn.close()
	