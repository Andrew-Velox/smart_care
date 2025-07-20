from django.contrib import admin
from .models import Doctor,Designation,Specialization,AvailableTime,Review
# Register your models here.

class SpecializationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Designation,DesignationModelAdmin)
admin.site.register(Specialization,SpecializationModelAdmin)


