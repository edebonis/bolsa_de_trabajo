from django.contrib import admin
from .models import Oportunidad, Tipo, Profile

# Register your models here.
# admin.site.register(Oportunidad)
admin.site.register(Tipo)
admin.site.register(Profile)


@admin.register(Oportunidad)
class Oportunidad(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'user', 'visible', 'tipo', 'fecha')
    list_editable = ('visible',)
    ordering = ('fecha',)