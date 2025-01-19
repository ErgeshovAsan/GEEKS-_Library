from django.shortcuts import render
from . import models
from django.views import generic


class AllBookView(generic.ListView):
    template_name = 'hastags/all_book.html'
    context_object_name = 'all_book'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all()


class FairyTaleBookView(generic.ListView):
    template_name = 'hastags/fairy_tale_book.html'
    context_object_name = 'fairy_tale_book'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Сказка')


class FantasticBookView(generic.ListView):
    template_name = 'hastags/fantastic_book.html'
    context_object_name = 'fantastic_book'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Фантастика')


class DramaBookView(generic.ListView):
    template_name = 'hastags/drama_book.html'
    context_object_name = 'drama_book'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Драмма')
