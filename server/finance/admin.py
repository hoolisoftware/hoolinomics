from django.contrib import admin

from . import models

@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.UnitCategory)
class UnitCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    change_list_template = 'entities/units_changelist.django-html'
    list_display = ('description', 'value', 'currency', 'category', 'datetime')
    date_hierarchy = 'datetime'
    list_filter = ('datetime', 'currency', 'category', )
