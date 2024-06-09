from django.contrib import admin
from django.utils.html import format_html

from trading_platform.models import Product, TradingLink


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_display_links = ['name', 'model']


@admin.register(TradingLink)
class TradingLinkAdmin(admin.ModelAdmin):
    """Админ-панель звена сети"""
    list_filter = ['city', 'level']
    list_display = ['id', 'name', 'type', 'city', 'level', 'arrear', 'supplier_link']
    actions = ['clear_arrear']

    def supplier_link(self, obj):
        """Функция отображения параметра related_link в качестве ссылки"""
        link = obj.supplier
        if link:
            return format_html('<a href="/admin/trading_platform/tradinglink/{}/change/">{}</a>', link.pk, link.name)
        else:
            return None

    @admin.action(description='Обнулить задолженность перед поставщиком')
    def clear_arrear(self, request, queryset):
        queryset.update(arrear=0.00)
