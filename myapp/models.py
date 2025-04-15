from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    phonenumber=models.CharField(max_length=70)
    FranchiseType=models.CharField(max_length=90, default="")
    Cityinterested=models.CharField(max_length=80, default="")


class bookappointment(models.Model):
    name=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    phonenumber=models.CharField(max_length=70)
    selectsalon=models.CharField(max_length=90, default="")
    selectservice=models.CharField(max_length=80, default="")
    appointmentdate=models.DateField(max_length=80, default="none",null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    userid=models.ForeignKey(User,  on_delete=models.CASCADE, blank=True, null=True)


    status = models.CharField(
        max_length=20,
        choices=[("upcoming", "Upcoming"), ("completed", "Completed"), ("cancelled", "Cancelled")],
        default="upcoming"
    )
    cancelreason=models.CharField(max_length=200, default="")

    def __str__(self):
        return f"Appointment for {self.name} {self.lastname} on {self.appointmentdate}"
    def cancel(self, reason):
        """Mark the appointment as canceled and save the reason."""
        self.status = "cancelled"
        self.cancelreason = reason
        self.save()






   


   




class blog(models.Model):
    title = models.CharField(max_length=200)
    desription=models.CharField(max_length=2000)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='blog/',default="")

    def __str__(self):
        return self.title
    
