from django.shortcuts import render
from . import models

def all_book(request):
    if request.method == 'GET':
        all_book = models.Book.objects.all()
        context = {'all_book': all_book}
        return render(request, template_name='hastags/all_book.html', context=context)

def fairy_tale_book(request):
    if request.method == 'GET':
        fairy_tale_book = models.Book.objects.filter(tags__name='Сказка')
        context = {'fairy_tale_book': fairy_tale_book}
        return render(request, template_name='hastags/fairy_tale_book.html', context=context)

def fantastic_book(request):
    if request.method == 'GET':
        fantastic_book = models.Book.objects.filter(tags__name='Фантастика')
        context = {'fantastic_book': fantastic_book}
        return render(request, template_name='hastags/fantastic_book.html', context=context)

def drama_book(request):
    if request.method == 'GET':
        drama_book = models.Book.objects.filter(tags__name='Драмма')
        context = {'drama_book': drama_book}
        return render(request, template_name='hastags/drama_book.html', context=context)
