from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models




def book_list(request):
    if request.method == 'GET':
        book_list = models.Books.objects.all(). order_by ('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)




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
