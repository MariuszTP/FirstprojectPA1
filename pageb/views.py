from django.shortcuts import render
from pageb.models import *
from django.db import models

from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def base(request):
    return render(request, 'base.html')

def main(request):

    if request.method =="POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        from_email = request.POST.get("from_email")
        data = {
            'subject' : subject,
            'message' : message,
            'from_email' : from_email,
        }
        message = '''
        New message:{}
        From: {}
        '''.format(data['message'], data['from_email'])
        send_mail(data['subject'], message, '', ['turekpython@gmail.com'])
       

    return render(request, 'index.html')

def gallery2(request):
    return render(request, 'gallery2.html')

    

""" def gallery1(request):
    products = Gallery1.objects.all()
    context = {'products': products}
    return render(request, 'gallery1.html', context) """



""" def gallery3(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery3.html', context)
 """
""" def gallery4(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery4.html', context) """

""" def gallery5(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery5.html', context) """


   