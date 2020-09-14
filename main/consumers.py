from channels.generic.websocket import AsyncWebsocketConsumer
import json
import psycopg2
from .models import data_esp
from .models import mac_adr



class MainConsumer(AsyncWebsocketConsumer):
#      self.groupname='dashboard'
      async def connect(self):
        self.groupname='dashboard'
                
        await self.channel_layer.group_add(
          self.groupname,
          self.channel_name,
        )
        await self.accept()

      async def disconnect(self, close_code):
        #await self.disconnect()
        pass

#      async def receive(self, text_data):
#        k=json.loads(text_data)
#        #b=temperatura(Number=k['Number'],Value=k['Value'])
#        conn = psycopg2.connect(dbname='myproject',
#            user='myprojectuser',
#            password='password',
#            host='localhost')
#        cur = conn.cursor()
#        cur.execute(
#        'INSERT INTO main_temperatura ("Number","Value","Time") VALUES (%s, %s, %s)',(k['Number'],k['Value'],k['Time'])
#        )
#        conn.commit()
#        conn.close()
#        #b.save()
#        print('>>>>>>>',text_data)

#        pass
      async def receive(self, text_data):
        k=json.loads(text_data)
        mac_prob=k['MAC']
        conn = psycopg2.connect(dbname='myproject',
          user='myprojectuser',
          password='password',
          host='localhost')
        cur = conn.cursor()
        lengs=len(k['Time'])
        cur.execute(
            'SELECT * FROM main_mac_adr WHERE "name" = %s',(mac_prob,)
          )
        t=cur.fetchone()
        if mac_prob==t[1]:
          for i in range(lengs):
            cur.execute(
              'INSERT INTO main_data_esp (mac_adr_id,"Value_mem","Value_t","Time") VALUES ((SELECT id FROM main_mac_adr WHERE "name"=%s), %s, %s, %s)',(k['MAC'],k['Value_mem'][i],k['Value_t'][i],k['Time'][i])
            )
            conn.commit()
        conn.close()

        pass