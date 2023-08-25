from django.contrib import admin

# Register your models here.

from .models import Ads, Category, Subcategory


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('type', )
    list_filter = ('type', )
    search_fields = ('title', 'description')
    

admin.site.register(Ads, AdsAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)