from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
#from .models import temperatura
#from .models import davlenie
#from .models import data_esp
from .models import mac_adr
from .models import data_esp_t
from .models import data_esp_mem
from rest_framework.decorators import api_view
import json
import psycopg2
#from django.views.decorators.http import require_http_methods




def index(request):
#	print('request: '+str(request.body))
	return render(request,'main/index.html')

@api_view(["GET","POST"])
def nkvm(request):
#	print('1: ',request)
#	print('2: ',str(request))
#	print('3: '+str(request.body))
	k=json.loads(request.body)
#	print('provEEEEEE: ', k['MAC'])
	mac_prob=k['MAC']
	conn = psycopg2.connect(dbname='myproject',
   		user='myprojectuser',
    	password='password',
	   	host='localhost')
	cur = conn.cursor()
	lengs_t=len(k['Temp_time'])
	lengs_mem=len(k['Axel_time'])
	cur.execute(
		'SELECT * FROM main_mac_adr WHERE "name" = %s',(mac_prob,)
		)
	t=cur.fetchone()
#	print('!!!!!!!!!!!',t)
	if mac_prob==t[1]:
		for i in range(lengs_t):
			cur.execute(
				'INSERT INTO main_data_esp_t (mac_adr_id,"Value_t","Time_t") VALUES ((SELECT id FROM main_mac_adr WHERE "name"=%s), %s, %s)',(k['MAC'],k['Temp'][i],k['Temp_time'][i])
				)
			conn.commit()
		for i in range(lengs_mem):
			cur.execute(
				'INSERT INTO main_data_esp_mem (mac_adr_id,"Value_mem","Time_mem") VALUES ((SELECT id FROM main_mac_adr WHERE "name"=%s), %s, %s)',(k['MAC'],k['Axel'][i],k['Axel_time'][i])
				)
			conn.commit()
		conn.close()
	return HttpResponse('111')


from django.db.models import Max


#def number_t(request):
#	number_t=temperatura.objects.aggregate(Max('Number'))
#	number_t=number_t['Number__max']
#	number_t=number_t+1
#	number_t=range(1,number_t)
#	context={'number_t':number_t}
#	return render(request, 'main/number_t.html', context)


#def temp_rub(request,num_t_id):
#	temp=temperatura.objects.filter(Number=num_t_id).order_by('-Time')
#	return render(request, 'main/temp_rub.html', {'temp':temp})


#def number_d(request):
#	number_d=davlenie.objects.aggregate(Max('Number'))
#	number_d=number_d['Number__max']
#	number_d=number_d+1
#	number_d=range(1,number_d)
#	context={'number_d':number_d}
#	return render(request, 'main/number_d.html', context)

#def davl_rub(request,num_d_id):
#	dav=davlenie.objects.filter(Number=num_d_id).order_by('-Time')
#	return render(request, 'main/davl_rub.html', {'dav':dav})
##########

#def number_mac(request):
#	number_mac=mac_adr.objects.all()
#	idl=range(len(number_mac))
#	context={'number_mac':number_mac, 'idl':idl}
#	return render(request, 'main/number_mac.html', context)

#def mac_rub(request,mac_id):
#	mac=data_esp.objects.filter(mac_adr=mac_id).order_by('-Time')
#	mac_name=mac[0].mac_adr
#	return render(request, 'main/mac_rub.html', {'mac':mac, 'mac_name': mac_name})

def number_mac_t(request):
	number_mac=mac_adr.objects.all()
	idl=range(len(number_mac))
#	num={}
#	for nam in range(i):
#		num[nam]=str(number_mac[nam])
	context={'number_mac':number_mac, 'idl':idl}
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
	return render(request, 'main/mac_rub_t.html', {'mac':mac, 'mac_name': mac_name})

def mac_rub_mem(request,mac_id):
	mac=data_esp_mem.objects.filter(mac_adr=mac_id).order_by('-Time_mem')
	mac_name=mac[0].mac_adr
	return render(request, 'main/mac_rub_mem.html', {'mac':mac, 'mac_name': mac_name})

