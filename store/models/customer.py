from django.db import  models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def register(self):
    	self.save

    @staticmethod
    def Customer.get_customer_by_username(username):
        try:
            return Customer.objects.filter(username=username)
        except:
            return False
    def isExists(self):
    	if Customer.objects.filter(email = self.email):
    		return True 
    	return False

