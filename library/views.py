from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views.generic import ListView
from django.views import generic



class SearchView(ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex


class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)




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
