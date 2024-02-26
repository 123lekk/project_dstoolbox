from django.urls import path
from . import views

urlpatterns = [
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('reserve_table/<int:table_number>/', views.reserve_table, name='reserve_table'),
    path('table_list/', views.table_list, name='table_list'),
    path('approve_reservation/<int:reservation_id>/', views.approve_reservation, name='approve_reservation'),
    path('reject_reservation/<int:reservation_id>/', views.reject_reservation, name='reject_reservation'),
    path('reset_reservations/', views.reset_reservations, name='reset_reservations'),
]