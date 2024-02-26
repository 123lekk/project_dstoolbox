from django.contrib import admin
from .models import Reservation, Table

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'table', 'email', 'phone', 'date', 'time', 'num_people', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'phone')

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)