from django.contrib import admin
from home.models import Servicos, Cargo, Equipe


@admin.register(Servicos)
class adminServicos(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Equipe)
class adminEquipe(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Cargo)
class adminCargo(admin.ModelAdmin):
    list_display = ('id',)
