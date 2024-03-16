from django.urls import path
from .views import *

urlpatterns = [
    path('',slide,name="slide" ),
    path('home/',home,name='home'),
    path('login/',sign_in,name='login'),
    path('logout/',sign_out,name='logout'),
    path('register/',Register , name='register'),
    path('profile/',profile,name='profile'),
    path('editprofile/',editprofile,name='editprofile'), 
    path('booking/<int:id>/',booking,name='booking'), 
    path('booking_list/',booking_list,name='booking_list'), 
    path('permissions/<int:id>/',permissions,name='permissions'),
    path('permissions_no/<int:id>/',permissions_no,name='permissions_no'),
    path('reset/',reset,name='reset'),
    path('cancel_booking/<int:id>/',cancel_booking,name='cancel_booking'),
    path('add_table/',add_table, name='add_table'), #เพิ่มโต๊ะ
    path('delete/<int:id>/',delete, name="delete"),
    

    # path('add_table_view/',add_table_view, name='add_table_view'),
]