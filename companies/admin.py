from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'ogrn', 'kpp', 'created_at')
    add_fieldsets = (
        (None, {'fields': ('name', 'inn', 'ogrn', 'kpp', 'addres') }),
    )
    search_fields = ('name', 'inn')
    ordering = ['name']
