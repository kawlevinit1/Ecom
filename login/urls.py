from django.urls import path
from . import views

urlpatterns = [
	path('register',views.register,name='register.html'),
	path('signin',views.signin,name='signin'),
	path('signup',views.signup,name='signup'),
	path('logout',views.logout,name='logout'),

]

