from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Job_list_Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def joblist(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Job_list_Contact(fname=fname,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request,'joblist.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(fname=fname,lname=lname,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request,'contact.html')
