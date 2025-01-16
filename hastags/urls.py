from django.urls import path
from . import views

urlpatterns = [
    path('all_book/', views.all_book, name='all_book'),
    path('fairy_tale_book/', views.fairy_tale_book, name='fairy_tale_book'),
    path('fantastic_book/', views.fantastic_book, name='fantastic_book'),
    path('drama_book/', views.drama_book, name='drama_book'),
]