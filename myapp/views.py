from django.shortcuts import render ,redirect, get_object_or_404
from myapp.forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# from .models import previousappointment
from django.contrib import messages



def signupview(request):
    if request.method == 'POST':    
        form = CustomuserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
           
            return redirect('/')
    else:
        form = CustomuserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required  # Ensures only logged-in users can access this page
def previousappointmentview(request):
    bookings = bookappointment.objects.filter(userid=request.user).order_by("-created_at")  # Fetch user-specific bookings

    return render(request, "previousappointment.html", {"bookings": bookings})


    
   

   





# Create your views here.
def homeview(request):
    return render(request,"home.html")
def aboutview(request):
    return render(request,"about.html")
def contactview(request):
    return render(request,"contact.html")
def websiteview(request):
    return render(request,"website.html")
def salonview(request):
    return render(request,"salon.html")
def offersview(request):
    return render(request,"offers.html")
def deleteappointmentview(request,id):
    return render(request,"deleteappointment.html",{'id':id})
def cancelappointmentview(request,id):
    if request.method == "POST":
        reason = request.POST.get("reason")

        appointment = get_object_or_404(bookappointment, id=id)

        if appointment.status != "Cancelled":
            appointment.cancel(reason)  # Call the cancel method
            messages.success(request, "Your appointment has been canceled.")
        else:
            messages.warning(request, "This appointment was already canceled.")

    
    return redirect("previousappointment")

def insertcontact(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})

def servicesview(request):
    return render(request,"services.html")

@login_required(login_url='/login/')
def bookappointmentview(request):
    return render(request,"bookappointment.html")


def newventureview(request):
    return render(request,"new venture.html")

def exploreproductview(request):
    return render(request,"explore product.html")

def insertbookappointment(request):
    if request.method=="POST":
        form=bookappointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/previousappointment')
    else:
        form=bookappointmentform()
    return render(request,"bookappointment.html",{'form':form})
def locateusview(request):
    return render(request,"locateus.html")  


def blogview(request):
    b=blog.objects.all()
    return render(request,"blog.html",{'b':b}) 

def blogdetailsview(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blogdetails.html",{'b':b}) 



  