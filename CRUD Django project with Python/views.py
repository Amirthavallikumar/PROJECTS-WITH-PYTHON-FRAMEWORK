from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas


# Create your views here.
def home(request):
    mydata = Datas.objects.all()
    if(mydata!=''):
        return render(request, 'index.html',{'datas': mydata})
    else:
        return render(request, 'index.html')

def adddata(request):

    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Mail = mail
        obj.Contact = contact
        obj.Address = address
        obj.save()
        mydata = Datas.objects.all()
        return redirect('home')
    return render(request,'index.html')

def updatedata(request,thisid):
    mydata = Datas.objects.get(id=thisid)
    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']
        mydata.Name=name
        mydata.Age=age
        mydata.Contact = contact
        mydata.Address = address
        mydata.Mail = mail
        mydata.save()
        return redirect('home')
    return render(request,'update.html',{'data':mydata})

def deletedata(request,thisid):
    mydata = Datas.objects.get(id=thisid)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        contact = request.POST['contact']
        mail = request.POST['mail']
        mydata.delete()
        return redirect('home')
    return render(request, 'delete.html', {'data': mydata})



