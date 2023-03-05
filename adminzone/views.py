from django.shortcuts import render,redirect
from myapp.models import Contact, AdminLogin
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    try:
        if request.session['name']:
            cust=Contact.objects.all()
            return render(request,'home.html',{'cust':cust})
    except KeyError:
        return render(request,'login.html')
    
def customer(request):
    try:
        if request.session['name']:
            cust=Contact.objects.all()
            return render(request,'customer.html',{'cust':cust})
    except KeyError:
        return render(request,'login.html')

def achangepassword(request):
    try:
        if request.session['name']:
            return render(request,'achangepassword.html')
    except KeyError:
        return render(request,'login.html')

def deletecust(request,id):
    cust = Contact.objects.get(id=id)
    cust.delete()
    return redirect('adminzone:customer')

def adminchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg='Message : '
    if newpassword!=confirmpassword:
        msg=msg+'New Password and Confirm password are not matched'
        return render(request,'achangepassword.html',{'msg':msg})
    name=request.session['name']
    try:
        admin=AdminLogin.objects.get(name=name,password=oldpassword)
        if admin is not None:
            ad=AdminLogin(name=name,password=newpassword)
            ad.save()
            return redirect('adminzone:logout')
    except ObjectDoesNotExist:
        msg=msg+'Old Password is not matched'
    return render(request, 'achangepassword.html', {'msg': msg})

def logout(request):
    try:
        if request.session['name']:
            request.session['name']=None
            return render(request,'login.html')
    except KeyError:
        return render(request,'login.html')

