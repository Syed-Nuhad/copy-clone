from django.contrib import admin
from .models import Filter

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'subcategory', 'keywords', 'min_price', 'max_price', 'autocop_enabled', 'created_at')
    list_filter = ('category', 'autocop_enabled')
    search_fields = ('keywords', 'user__username')
