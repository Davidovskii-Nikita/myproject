from django.urls import path
from . import views
			

urlpatterns = [
	path('', views.index, name='main'),
#	path('number_t/', views.number_t, name='name_t'),
#	path('number_t/t<int:num_t_id>', views.temp_rub),
#	path('number_d/', views.number_d, name='name_d'),
#	path('number_d/d<int:num_d_id>', views.davl_rub),
#	path('number_mac/', views.number_mac, name='name_mac'),
#	path('number_mac/<int:mac_id>', views.mac_rub),
	path('nkvm',views.nkvm),
	path('number_mac_t/', views.number_mac_t, name='name_mac_t'),
	path('number_mac_mem/', views.number_mac_mem, name='name_mac_mem'),
	path('number_mac_t/<int:mac_id>', views.mac_rub_t),
	path('number_mac_mem/<int:mac_id>', views.mac_rub_mem)
]
