from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('index',views.index,name='index'),
	path('collection',views.collection,name='collection'),
	path('collection2',views.collection2,name='collection2'),
	path('checkout',views.checkout,name='checkout'),
	path('contact',views.contact,name='contact'),
	path('about',views.about,name='about'),
	path('spd',views.spd,name='spd'),
	
]