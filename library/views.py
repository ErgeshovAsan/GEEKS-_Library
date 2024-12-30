from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("My name is Asan")

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://img.ridus.ru/images2/14/87/61487_1600x1020.webp'>")

def date_time(request):
    if request.method == 'GET':
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return HttpResponse(f"The current date and time is: {current_time}")
