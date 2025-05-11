from django.db import models

class Company(models.Model):
    name = models.CharField('Название компании', max_length=255, unique=True)
    inn = models.CharField('ИНН', max_length=12, unique=True)
    ogrn = models.CharField('ОГРН', max_length=13, blank=True, null=True)
    kpp = models.CharField('КПП', max_length=9, blank=True, null=True)
    addres = models.CharField('Адрес регистрации', max_length=512, blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']

    def __str__(self):
        return self.name

        