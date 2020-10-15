from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.http import HttpResponse
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password ,check_password
# Create your views here.

def register(request):
	return render(request,'register.html',)

def logout(request):
    auth.logout(request)
    return redirect('/')


def signin(request):
    if request.method=='GET':
        return render(request,'register.html')

    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        customer = Customer.get_by_username(username)
        error_message = None

        if customer:
            flag = check_password(password ,customer.password)

            if flag:
                return redirect('/index')
            else:
                error_message = 'Email or Password Invalid'

        else:
            error_message = 'Email or Password Invalid'

    return render(request,'index.html',{'error':error_message})

def signup(request):
    if request.method == 'GET':

        return render(request,'register.html')

    else:
        postData = request.POST
        username = postData.get('username')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(username,phone,email,password)
        #valdation
        
        value = {
            'username':username,
            'phone':phone,
            'email':email,
        }
        error_message =None
        customer = Customer(username=username,phone=phone,email=email,password=password)
        if (not username):
            error_message =  "Username Required"
        elif len(username) < 4:
            error_message ="Username must be 4 char or long"
        
        isExists = customer.isExists()
        if isExists:
            error_message = 'Email Already taken'
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return render(request,'register.html')
        else:
            data = {
                    'error':error_message,
                    'values':value
            }
            return render(request,'register.html', data)