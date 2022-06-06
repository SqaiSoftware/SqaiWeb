from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


# Create your views here.


def index(request):
    return render(request, 'sqai/index.html')


def contact(request):
    if (request.method == 'POST'):
        subject = "Website Inquiry"
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        body = f'{name}\n{email}\n{subject}\n{message}'

        try:
            send_mail(subject, body, settings.EMAIL_HOST_USER, ['info@sqaisoftwares.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return render(request, 'sqai/contact.html', {'name': name})

    else:
        return render(request, 'sqai/contact.html')


def portfolio(request):
    return render(request, 'sqai/portfolio.html')