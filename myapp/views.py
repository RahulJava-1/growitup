from django.shortcuts import render,redirect,reverse
from . models import Contact, AdminLogin
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contact(request):
        name=request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        choose = request.POST.get('choose')
        con = Contact(name=name, email=email, phone=phone,choose=choose)
        con.save()
        return redirect(reverse('index'))

def validateadmin(request):
    name = request.POST['name']
    password = request.POST['password']
    msg=''
    try:
        admin = AdminLogin.objects.get(name=name,password=password)
        if admin is not None:
            request.session['name']=name
            return redirect(reverse('adminzone:home'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'login.html',{'msg':msg})
