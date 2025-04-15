from django.contrib import admin
from myapp.models import *



# Register your models here.
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass

 
@admin.register(bookappointment)
class bookappointmentadmin(admin.ModelAdmin):
    list_display=('name','email','phonenumber','selectsalon','selectservice','appointmentdate','userid','status')


   

    


   