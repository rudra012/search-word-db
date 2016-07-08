from django.contrib import admin

# Register your models here.
from demo.models import Deals


@admin.register(Deals)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'location', 'original_price', 'price')
    search_fields = ('title', 'link', 'location',)
    readonly_fields = list_display
    fields = list_display