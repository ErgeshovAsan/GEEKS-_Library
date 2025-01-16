from django.db import models
from library.models import Books

class OrderModel(models.Model):
    CHECK = (
        ("Курьер", "Курьер"),
        ("Самовывоз", "Самовывоз"),
    )
    name = models.CharField(max_length=100, verbose_name='Имя и Фамилия', null=True)
    phon = models.CharField(max_length=16, verbose_name='Номер телефона', null=True)
    checked = models.CharField(verbose_name='Доставка', choices=CHECK, max_length=10)
    delivery_address = models.CharField(max_length=150, verbose_name='Адрес доставки', null=True)
    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Название и цена книги')
    quantity = models.PositiveIntegerField(verbose_name='Кольичество', max_length=100, null=True)
    promo_code = models.CharField(verbose_name='Промокод', max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.choice_book} - {self.checked}'