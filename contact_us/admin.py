from django.contrib import admin
from .models import ContactUs
# Register your models here.


class ContacModelAdmin(admin.ModelAdmin):
    list_display = ['name','phone']

admin.site.register(ContactUs,ContacModelAdmin)