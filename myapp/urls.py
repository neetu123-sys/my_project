from django.urls import path
from myapp.views import *
from django.contrib.auth import views as auth_views
# from .views import previousappointment



urlpatterns=[
    path('home',homeview),
     path('about',aboutview),
     path('contact/',contactview),
        path('website',websiteview),
        path('',salonview),
         path('offers',offersview),
         path('blog',blogview),
         path('blogdetails/<int:id>/',blogdetailsview),
          path('insertcontact',insertcontact ),
          path('services',servicesview),
         path('explore product',exploreproductview),
          path('new venture',newventureview),
        path('bookappointment',bookappointmentview),
           path('insertbookappointment',insertbookappointment),
             path('deleteappointment/<int:id>',deleteappointmentview, name='deleteappointment'),
              path('cancelappointment/<int:id>',cancelappointmentview, name='cancelappointment'),
           path('locateus',locateusview),
          path("previousappointment/", previousappointmentview, name="previousappointment"),
           path('login/', auth_views.LoginView.as_view(), name='login'),
           path('logout/', auth_views.LogoutView.as_view(), name='logout'),
           path('signup/',signupview, name='signup'),
]


