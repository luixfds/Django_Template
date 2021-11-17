import variable as variable
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
        abstract = True


class Servicos(Base):
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


class Equipe:
    name = models.CharField(max_length=30)
    cargo = models.ForeignKey(Cargo, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    facebook = models.CharField('Facebook', max_length=200, default='#')
    twitter = models.CharField('Twitter', max_length=200, default='#')
    instagram = models.CharField('Instagram', max_length=200, default='#')
    foto = StdImageField('Foto', upload_to=troca_nome, validators={'thumb': {'widht': 400, 'height': 400}})

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.name

