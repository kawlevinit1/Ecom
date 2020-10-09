from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from store.models.product import Product 
from store.models.product import Category
# Create your views here.

def home(request):
	products = Product.get_all_products();
	return render(request,'index.html',{'products':products})

def index(request):
	products = Product.get_all_products();
	return render(request,'index.html',{'products':products})

def checkout(request):
	return render(request,'checkout.html')

def contact(request):
	return render(request,'contact.html')

def collection(request):
	products = None
	categories = Category.get_all_categories();
	categoryID = request.GET.get('Category')
	if categoryID:
		products = Product.get_all_products_by_categoryid(catagoty_id)
	else:
		products = Product.get_all_products();
	data = {}
	data['products'] = products
	data['categories'] = categories
	return render(request,'collection.html',data)

def collection2(request):
    return render(request,'collection2.html')

def about(request):
	return render(request,'about.html')

def spd(request):
	return render(request,'spd.html')

