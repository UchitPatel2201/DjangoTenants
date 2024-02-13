from django.contrib import admin
from .models import SweetType

# Register your models here.
@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
