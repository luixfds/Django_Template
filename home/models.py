from django.db import models
from stdimage import StdImageField
import uuid


def troca_nome(_instance, filename):
    tipo_ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{tipo_ext}'
    return filename


class Base(models.Model):
    criado = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        Abstract = True


class Serviços(Base):
    ICONES = (
        ('ini-cog', 'Engrenagem'),
        ('ini-stats-up', 'Grafico'),
        ('ini-users', 'Configurações'),
        ('ini-layers', 'Designer'),
        ('ini-mobile', 'Mobilete'),
        ('ini-rocket', 'Foguetin'),
    )
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    icone = models.CharField(max_length=12, choices=ICONES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo


class Cargo(Base):
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo