from django.contrib import admin
from .models import Category, Equipment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('inventory_number', 'name', 'category', 'status', 'added_date')
    list_filter = ('category', 'status')
    search_fields = ('inventory_number', 'name')