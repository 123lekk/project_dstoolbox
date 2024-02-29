from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('reservation_list/', views.reservation_list, name='reservation_list'),
    path('reserve_table/<str:table_name>/', views.reserve_table, name='reserve_table'),
    path('table_list/', views.table_list, name='table_list'),
    path('approve_reservation/<int:reservation_id>/', views.approve_reservation, name='approve_reservation'),
    path('reject_reservation/<int:reservation_id>/', views.reject_reservation, name='reject_reservation'),
    path('reset_reservations/', views.reset_reservations, name='reset_reservations'),
    path('commit_list/', views.commit_list, name='commit_list'),
    path('add_table/', views.add_table, name='add_table'), #เพิ่มโต๊ะ
    path('add_table_view/', views.add_table_view, name='add_table_view'), #ดึงหน้า เพิ่มโต๊ะ มาแสดง
]