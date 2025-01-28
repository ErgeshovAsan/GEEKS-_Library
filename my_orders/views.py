from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class CreateOrderView(generic.CreateView):
    template_name = 'order/create_order.html'
    form_class = forms.OrderForm
    success_url = '/order_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)


@method_decorator(cache_page(60*15), name='dispatch')
class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'order_list'
    model = models.OrderModel

    def get_queryset(self):
        orders = cache.get('orders')
        if not orders:
            orders = self.model.objects.all().order_by("-id")
            cache.set('orders', orders, 60*15)
        return orders


class OrderDetailView(generic.DetailView):
    template_name = 'order/order_detail.html'
    context_object_name = 'order_id'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderModel, id=order_id)


class OrderUpdateView(generic.UpdateView):
    template_name = 'order/update_order.html'
    form_class = forms.OrderForm
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderModel, id=order_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderUpdateView, self).form_valid(form=form)


class DeleteOrderView(generic.DeleteView):
    template_name = 'order/confirm_delete.html'
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderModel, id=order_id)