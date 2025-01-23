from django.urls import path
from . import views

urlpatterns = [
    path('mybook_list/', views.MybookListView.as_view(), name='mybook_list'),
    path('mybook_form/', views.MybookFormView.as_view(), name='mybook_form'),
]