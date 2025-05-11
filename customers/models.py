from django.db import models
from django.conf import settings

class Status(models.Model):
    name = models.CharField('Статус', max_length=100, unique=True)
    color = models.CharField(max_length=7, verbose_name='Цвет (HEX)', help_text='#RRGGBB')  # HEX-цвет: #RRGGBB
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField('Тег', max_length=100, unique=True)
    color = models.CharField(max_length=7, verbose_name='Цвет (HEX)', help_text='#RRGGBB') # HEX-цвет: #RRGGBB

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    last_name = models.CharField('Фамилия', max_length=255)
    first_name = models.CharField('Имя', max_length=255)
    middle_name = models.CharField('Отчество', max_length=255)
    email = models.EmailField('Электронная почта', max_length=255, blank=True)
    phone = models.CharField('Номер телефона', max_length=20, blank=True)
    
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Менеджер', related_name='customers')
    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, null=True, verbose_name='Компания', related_name='customers', blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, verbose_name='Статус', related_name='customers')
    tags = models.ManyToManyField(Tag, related_name='customers', blank=True, verbose_name='Теги')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return f'Заказчик: {self.last_name} {self.first_name}\nЭлектронная почта: {self.email}\nНомер телефона: {self.phone}'
    
    