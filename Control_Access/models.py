from django.db import models
from django.contrib.auth.models import User # Importe o modelo user


# Create your models here.
class Usuario(models.Model):
    # Este campo cria relação de 'um para um' com o modelo User do Django
    # Cada Administrador ESTÁ LIGADO a um único User
    # A classe Usuario seria uma classe especializada do User
    # Usando OneToOneField, garantimos que cada usuário tenha no máximo um administrador associado
    # models.CASCADE garante que se o usuário for deletado, o administrador também será

    # A classe User já possui, entre outros, os campos: username, password, email, first_name, last_name
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # Campos adicionais para a classe usuario

    # Para pessoa fisica
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)

    # Para pessoa Jurídica
    CNPJ = models.CharField(max_length=14, unique=True, null=True, blank=True)

    # Campo para armazenar a data de nascimento do usuário
    data_nascimento = models.DateField()

    # Campo para armazenar o telefone do usuário
    telefone = models.CharField(max_length=15)

    # Campo para armazenar o endereço do usuário
    rua = models.CharField(max_length=255)
    numero_casa = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    # O campo de nome e email já existem no modelo User, então não precisa repetir.
    # E o mais importante: A SENHA será gerenciada pelo modelo User do Django

    # Área de Métodos
    
    def __str__(self):
        return self.user.username
    
