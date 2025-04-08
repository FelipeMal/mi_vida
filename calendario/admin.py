from django.contrib import admin
from .models import Mes, FotoMes, CancionMes, Nota

class FotoMesInline(admin.TabularInline):
    model = FotoMes
    extra = 1

class CancionMesInline(admin.TabularInline):
    model = CancionMes
    extra = 1

class NotaInline(admin.TabularInline):
    model = Nota
    extra = 1

@admin.register(Mes)
class MesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_creacion']
    list_filter = ['fecha_creacion']
    search_fields = ['nombre', 'mensaje']
    inlines = [FotoMesInline, CancionMesInline, NotaInline]

@admin.register(FotoMes)
class FotoMesAdmin(admin.ModelAdmin):
    list_display = ['mes', 'descripcion', 'fecha_subida']
    list_filter = ['mes', 'fecha_subida']
    search_fields = ['descripcion']

@admin.register(CancionMes)
class CancionMesAdmin(admin.ModelAdmin):
    list_display = ['mes', 'titulo', 'fecha_subida']
    list_filter = ['mes', 'fecha_subida']
    search_fields = ['titulo']
