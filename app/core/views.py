from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse


from .models import *
from .models import FeedBackMain
from django.core.mail import send_mail
from .forms import *
from test_work import settings




def index(request):
    context = { 
    'title_page' : 'Форма отправки сообщений 1.0'
    }
    return render(request, 'core/index.html', context)


#Отрисовка формы и отправка сообщения в бд и почту
class ContactFormView(View):
   def post(self, request):
        form = ContactForm(request.POST)
        data = form.data
        subject =  f'Сообщение с формы от {data["name"]} '
        body_message = f' Имя сайта: {data["domain_name"]} Почта отправителя: {data["email"]} Описание проблемы: {data["description"]} Телефон: {data["phone"]} Откуда узнали: {data["inform"]}'
        if form.is_valid():
            form.save()
            email(subject, body_message)
            messages.add_message(request, settings.MY_INFO, 'Cообщение успешно отправлено')
        else:
             messages.add_message(request, settings.MY_INFO, 'Сообщение не было отправлено')   

        return redirect('/')         
     
# Функция отправки сообщения
def email(subject, content):
   send_mail(subject, content,'djangosendmailv3@gmail.com',['aspidsec@gmail.com'])    