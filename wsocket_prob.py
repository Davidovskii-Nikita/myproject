import json
import requests
import redis
import websocket
import datetime

ws=websocket.WebSocket()

import random, time

ws.connect(
	"ws://0.0.0.0/ws/data/"
	)

for i in range(3):
	time.sleep(1)

	ws.send(json.dumps({
		'MAC': 'MAC: 123-456-789',
		'Value_mem':[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)],
		'Value_t':[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)],
		'Time':[str(datetime.datetime.today()),str(datetime.datetime.today()),str(datetime.datetime.today()),str(datetime.datetime.today())]
		}))
