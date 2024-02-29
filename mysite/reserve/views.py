from django.shortcuts import render, redirect
from .models import *
from .forms import ReservationForm
from datetime import datetime, time

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reserve/reservation_list.html', {'reservations': reservations})

def reserve_table(request, table_name):
    table = Table.objects.get(table_name=table_name)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = table
            reservation.save()
            table.is_reserved = True
            table.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reserve/reserve_table.html', {'form': form, 'table': table})

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'reserve/table_list.html', {'tables': tables})

def approve_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.status = 'ยอมรับ'
    reservation.save()
    return redirect('reservation_list')

def reject_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.status = 'ปฏิเสธ'
    reservation.save()
    return redirect('reservation_list')

def reset_reservations(request):
    
    current_time = datetime.now().time()
    if current_time >= time(18, 0) and current_time <= time(21, 0):
        Reservation.objects.all().delete()
        Table.objects.all().update(is_reserved=False)

    return redirect('table_list')

# def commit_list(req):
#     return render(req, 'reseve/commit_list.html')

def commit_list(request):
    tables = Table.objects.all()
    return render(request, 'reserve/commit_list.html',{'tables': tables})

#เพิ่มชื่อโต้ะลง database
def add_table(req):
    if req.method == 'POST':
        table_name = req.POST.get('add_table')
        print(table_name)

        add_table = Table.objects.create(
            table_name = table_name,
            is_reserved = False,
        )
        add_table.save()
        return redirect(req, 'reserve/commit_list')
    return render(req, 'reserve/commit_list.html')

#ดึงหน้า เพิ่มโต๊ะ มาแสดง
def add_table_view(request):
    return render(request, 'reserve/add_table.html')