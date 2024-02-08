from django.contrib import admin

# Register your models here.
from .models import *
class FreeTrilerAdmin(admin.ModelAdmin):
    # Optionally customize the admin options for your model
    list_display = ['name','windoid','start','expire','finish']  # Example: customize the fields displayed in the list view

admin.site.register(FreeTriler,FreeTrilerAdmin)