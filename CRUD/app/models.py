from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField('nome', max_length=40)
    telefone = models.IntegerField('telefone')
    email = models.EmailField('email')

    def __str__(self):
        return f'Nome:{self.nome}, telefone:{self.telefone}, email:{self.email}'
