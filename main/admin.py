from django.contrib import admin

#from .models import temperatura
#from .models import davlenie
#from .models import data_esp
from .models import mac_adr
from .models import data_esp_mem
from .models import data_esp_t

#class temperaturaAdmin(admin.ModelAdmin):
#	list_display = ('Number', 'Value', 'Time')

#class davlenieAdmin(admin.ModelAdmin):
#	list_display = ('Number', 'Value', 'Time')

#class dataespAdmin(admin.ModelAdmin):
#	list_display = ('mac_adr', 'Value_mem', 'Value_t', 'Time')

class macadrAdmin(admin.ModelAdmin):
	list_display = ('name','id')

class dataesptAdmin(admin.ModelAdmin):
	list_display = ('mac_adr', 'Value_t', 'Time_t')

class dataespmemAdmin(admin.ModelAdmin):
	list_display = ('mac_adr', 'Value_mem', 'Time_mem')




#admin.site.register(temperatura, temperaturaAdmin)
#admin.site.register(davlenie, davlenieAdmin)
#admin.site.register(data_esp, dataespAdmin)
admin.site.register(mac_adr, macadrAdmin)
admin.site.register(data_esp_t, dataesptAdmin)
admin.site.register(data_esp_mem, dataespmemAdmin)

# Register your models here.
