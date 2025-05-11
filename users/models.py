from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        MANAGER = 'manager', 'Менеджер'
        
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.MANAGER)
    
    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser
    
    def is_manager(self):
        return self.role == self.Roles.MANAGER