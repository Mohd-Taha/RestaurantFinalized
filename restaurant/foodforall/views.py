from django.shortcuts import render,redirect
from django.http import  HttpResponse

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
# from .models import Product
from .models import Team
from .models import order
from .models import testimonial
from .models import featured
from .models import products
from .models import starters
from math import ceil


def index(request):
    team = Team.objects.all()
    print(team)
    n=len(team)
    nSlides = n//4 + ceil((n/4)-(n//4))
    feature = featured.objects.all()
    

    params = { 'no_of_slides':nSlides,'range':range(nSlides),'teams':team }
    return render(request, 'index.html',{'params':params,'feature':feature})

def sendmail(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        subj = 'Queries'
        info = "Fullname" + name + "Email" + email + "Subject" + subject + "Query" + message
        email_from= settings.EMAIL_HOST_USER
        recipent_list = ['samiha.pirani@gmail.com']
        send_mail(subject,info,email_from,recipent_list)

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def about(request):
    abt=Team.objects.all()
    chef={
        'abt':abt
    }
    return render(request, 'about.html',chef)

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def booking(request):
    return render(request, 'booking.html')

def menu(request):
    start=starters.objects.all()

    # men1={
    #     'start':start
    # }
    return render(request, 'menu.html',{'start':start})

def product(request,id):
    prod = products.objects.get(id=id)
    return render(request, 'products.html',{'prod':prod})


def team(request):
    return render(request, 'team.html')

def review(request):
    obj=testimonial.objects.all()
    context={
        'obj':obj
    }
    return render(request, 'review.html',context)

def orders(request):
    product = order.objects.all()
    print(product)
    n=len(product)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # 'no_of_slides':nSlides,'range':range(nSlides),
    return render(request, 'orders.html',{'product':product})

def products_detail(request, pk):
    pr = products.objects.all()
    return render(request, 'products_detail.html', {'pr': pr})

