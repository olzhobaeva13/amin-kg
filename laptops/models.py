from django.db import models
from laptops.choices import LAPTOP_TYPES


class Laptop(models.Model):
    name = models.CharField(max_length=220, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    type = models.CharField(max_length=22, choices=LAPTOP_TYPES)
    pictures = models.ImageField(upload_to='amen-kg/laptops', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    
    def __str__(self) -> str:
        return self.name