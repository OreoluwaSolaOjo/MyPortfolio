from django import template
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from MyPortfolio.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('txtName')
        email = request.POST.get('txtEmail')
        phone = request.POST.get('txtPhone')
        subject = request.POST.get('txtMsg')
        contact.txtName = name
        contact.txtEmail = email
        contact.txtPhone = phone
        contact.txtMsg = subject
        contact.save()
        template = render_to_string(
            'portfolio/email_template.html', {'name': name})
        email = EmailMessage(
            'Thank you for contacting me',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        email.send()

        return thankyoupage(request)
    else:
        return render(request, 'portfolio/index.html')


def thankyoupage(request):
    return render(request, 'portfolio/thankyoupage.html')


def restaurant(request):
    return render(request, 'portfolio/portfolio-restaurant-website.html')


def fitnessbyore(request):
    return render(request, 'portfolio/portfolio-fitnessbyore-website.html')


def galaxybyosg(request):
    return render(request, 'portfolio/portfolio-galaxygamebyosg-application.html')


def bmicalculator(request):
    return render(request, 'portfolio/portfolio-bodymasscalculator-application.html')
