from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=15, unique=True, primary_key=True)
    class Meta:
        db_table = 'usuario'
    class criarUsuario(BaseUserManager):
        def create_user(self, cpf, password=None, **extra_fields):
            if not cpf:
                raise ValueError('Cpf')
            user = self.model(cpf = cpf, **extra_fields)
            user.set_password(password)
            user.save()
