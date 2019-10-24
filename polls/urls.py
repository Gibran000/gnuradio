from django.conf.urls import url
from django.urls import path
from . import views
#from gnuradio.urls import views

urlpatterns = [
    path('', views.index, name='index'),
	path('services', views.services, name='services'),
	path('about', views.about, name='about'),
	path('bloque', views.bloque, name='bloque'),
	path('pruebas', views.pruebas, name='pruebas'),
	path('instalacion', views.instalacion, name='instalacion'),
]
