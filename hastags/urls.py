from django.urls import path
from . import views

urlpatterns = [
    path('all_book/', views.AllBookView.as_view(), name='all_book'),
    path('fairy_tale_book/', views.FairyTaleBookView.as_view(), name='fairy_tale_book'),
    path('fantastic_book/', views.FantasticBookView.as_view(), name='fantastic_book'),
    path('drama_book/', views.DramaBookView.as_view(), name='drama_book'),
]