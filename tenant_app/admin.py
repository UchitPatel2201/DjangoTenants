from django.contrib import admin
from .models import Sweet

# Register your models here.
@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = ['name',]
