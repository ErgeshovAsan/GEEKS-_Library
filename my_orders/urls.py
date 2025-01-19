from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('order_list/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order_list/<int:id>/update/', views.OrderUpdateView.as_view(), name='update_order'),
    path('order_list/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
    ]
