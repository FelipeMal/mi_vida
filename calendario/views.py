from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Mes, FotoMes, CancionMes, Nota
import os

def calendario_view(request):
    meses = Mes.objects.all().order_by('fecha_creacion')
    return render(request, 'calendario/calendario.html', {'meses': meses})

def detalle_mes_view(request, mes_nombre):
    mes = get_object_or_404(Mes, nombre=mes_nombre)
    return render(request, 'calendario/detalle_mes.html', {'mes': mes})

@login_required
def admin_dashboard(request):
    meses = Mes.objects.all().order_by('fecha_creacion')
    return render(request, 'calendario/admin_dashboard.html', {'meses': meses})
