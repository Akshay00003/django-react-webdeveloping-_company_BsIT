from django.contrib import admin
from .models import Appoinment
# Register your models here.



class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'booked_on' )
admin.site.register(Appoinment, AppoinmentAdmin)