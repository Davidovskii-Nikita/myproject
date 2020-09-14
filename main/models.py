from django.db import models


#class temperatura(models.Model):
#	Number=models.IntegerField(null=True, verbose_name='Nomer')
#	Value=models.FloatField(null=True, blank=True, verbose_name='Velichina')
#	Time=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Vremya dobavleniya')

#class davlenie(models.Model):
#	Number=models.IntegerField(null=True, verbose_name='Nomer')
#	Value=models.FloatField(null=True, blank=True, verbose_name='Velichina')
#	Time=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Vremya dobavleniya')

#class data_esp(models.Model):
#	mac_adr=models.ForeignKey('mac_adr', on_delete=models.PROTECT, verbose_name='mac adres')
#	Value_mem=models.FloatField(null=True, blank=True, verbose_name='Velichina mems')
#	Value_t=models.FloatField(null=True, blank=True, verbose_name='Velichina temp')
#	Time=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Vremya dobavleniya')

class mac_adr(models.Model):
	name=models.CharField(max_length=50, null=True, blank=True, verbose_name='mac adres')
	
	def __str__ (self):
		return self.name

class data_esp_t(models.Model):
	mac_adr=models.ForeignKey('mac_adr', on_delete=models.PROTECT, verbose_name='mac adres')
	Value_t=models.FloatField(null=True, blank=True, verbose_name='Velichina temp')
	Time_t=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Vremya dobavleniya')




class data_esp_mem(models.Model):
	mac_adr=models.ForeignKey('mac_adr', on_delete=models.PROTECT, verbose_name='mac adres')
	Value_mem=models.FloatField(null=True, blank=True, verbose_name='Velichina temp')
	Time_mem=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Vremya dobavleniya')

#	def __str__ (self):
#		return self.name