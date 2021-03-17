from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import mac_adr
from .models import data_esp_t
from .models import data_esp_mem
from rest_framework.decorators import api_view
import json
import psycopg2
import datetime
import time
from datetime import timezone

def index(request):
	return render(request,'main/index.html')

@api_view(["GET","POST"])
def nkvm(request):
	k=json.loads(request.body)
	print(k)
	mac_prob=k['MAC']
	conn = psycopg2.connect(dbname='postgres',
   		user='postgres',
    	password='admin',
	   	host='localhost')
	cur = conn.cursor()
	lengs_t=len(k['Temp_time'])
	lengs_mem=len(k['Axel_time'])
	cur.execute(
		'SELECT * FROM main_mac_adr WHERE "name" = %s',(mac_prob,)
		)
	t=cur.fetchone()
	if mac_prob==t[1]:
		for i in range(lengs_t):
			cur.execute(
				'INSERT INTO main_data_esp_t (mac_adr_id,"Value_t","Time_t") VALUES ((SELECT id FROM main_mac_adr WHERE "name"=%s), %s, %s)',(k['MAC'],k['Temp'][i],datetime.datetime.utcfromtimestamp(int(k['Temp_time'][i])))
				)
			conn.commit()
		for i in range(lengs_mem):
			cur.execute(
				'INSERT INTO main_data_esp_mem (mac_adr_id,"Value_mem","Time_mem") VALUES ((SELECT id FROM main_mac_adr WHERE "name"=%s), %s, %s)',(k['MAC'],k['Axel'][i],datetime.datetime.utcfromtimestamp(int(k['Axel_time'][i]))
				))
			conn.commit()
		conn.close()
	return HttpResponse('111')


from django.db.models import Max




def number_mac_t(request):
	number_mac=mac_adr.objects.all()
	idl=range(len(number_mac))
	context={'number_mac':number_mac, 'idl':idl, 'id':id}
	return render(request, 'main/number_mac_t.html', context)

def number_mac_mem(request):
	number_mac=mac_adr.objects.all()
	idl=range(len(number_mac))
#	num={}
#	for nam in range(i):
#		num[nam]=str(number_mac[nam])
	context={'number_mac':number_mac, 'idl':idl}
	return render(request, 'main/number_mac_mem.html', context)

def mac_rub_t(request,mac_id):
	mac=data_esp_t.objects.filter(mac_adr=mac_id).order_by('-Time_t')
	mac_name=mac[0].mac_adr
	id=mac[0].id
	return render(request, 'main/mac_rub_t.html', {'mac':mac, 'mac_name': mac_name, 'id':id})

def mac_rub_mem(request,mac_id):
	mac=data_esp_mem.objects.filter(mac_adr=mac_id).order_by('-Time_mem')
	mac_name=mac[0].mac_adr
	return render(request, 'main/mac_rub_mem.html', {'mac':mac, 'mac_name': mac_name})

def graf_t(request,mac_id):
	mac = data_esp_t.objects.filter(mac_adr=mac_id).order_by('Time_t')
	dlin=len(mac)
	time=[i.Time_t.strftime("%m.%d.%Y %H:%M:%S") for i in mac]
	value=[i.Value_t for i in mac]
	mac_name = mac[0].mac_adr
	k=''
	x=[]
	y=[]
	for i in mac:
		x.append(i.Time_t.timestamp())
		y.append(i.Value_t)
		k=k+'{'+str(i.Time_t.timestamp())+','+str(i.Value_t)+'}'
		if i!= mac[len(mac)-1]:
			k=k+','
	dlin=len(x)
	print(x)
	print('asd: ',y)
	posle_zap = 2
	ed_izmer='°C'
	return render(request, 'main/graf.html', {'time':time, 'value':value, 'k':k, 'x':x, 'y':y, 'dlin':dlin, 'posle_zap':posle_zap, 'ed_izmer':ed_izmer})

def graf_mem(request,mac_id):
	mac = data_esp_mem.objects.filter(mac_adr=mac_id).order_by('Time_mem')
	dlin=len(mac)
	time=[i.Time_mem.strftime("%m.%d.%Y %H:%M:%S") for i in mac]
	value=[i.Value_mem for i in mac]
	mac_name = mac[0].mac_adr
	posle_zap=2
	ed_izmer='м/сек2'
	k = ''
	x = []
	y = []
	for i in mac:
		x.append(i.Time_mem.timestamp())
		y.append(i.Value_mem)
		k = k + '{' + str(i.Time_mem.timestamp()) + ',' + str(i.Value_mem) + '}'
		if i != mac[len(mac) - 1]:
			k = k + ','
	dlin = len(x)
	print(x)
	print('asd: ', y)
	return render(request, 'main/graf.html', {'time':time, 'value':value, 'k':k, 'x':x, 'y':y, 'dlin':dlin, 'posle_zap':posle_zap, 'ed_izmer':ed_izmer})



