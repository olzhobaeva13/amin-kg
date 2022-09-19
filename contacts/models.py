from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=220, verbose_name='Адрес')
    phone_number = models.CharField(max_length=220, verbose_name='Номер телефона')

    telegram = models.URLField(verbose_name='Телеграм')
    linedin = models.URLField(verbose_name='Линкедин')
    instagram = models.URLField(verbose_name='Инстаграм')
    youtube = models.URLField(verbose_name='Ютуб')

    map_picture = models.ImageField(upload_to='amin-kg/contacts', null=True,
                                    blank=True, verbose_name='Изображение карты')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    
    def __str__(self) -> str:
        return self.address
