from django.contrib import admin

from .models import *

@admin.register(Phone)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'status')

@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    list_display = ('images',)

@admin.register(Tablet)
class TabletsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'status')

@admin.register(TabletImage)
class TabletsImageAdmin(admin.ModelAdmin):
    list_display = ('images',)

    
