from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        MANAGER = 'manager', 'Менеджер'
        
    role = models.CharField('Роль', max_length=20, choices=Roles.choices, default=Roles.MANAGER)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username', 'role', 'is_staff']
    
    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser
    
    def is_manager(self):
        return self.role == self.Roles.MANAGER
    
    def __str__(self):
        return self.username