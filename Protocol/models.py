from django.db import models
from django.contrib.auth.models import User # Importe o modelo user


class processo_administrativo(models.Model):
    # Campo de chave primária 'protocolo' que é auto-incrementado
    protocolo = models.IntegerField(primary_key=True, auto_created=True)
    
    # Definindo as opções para o campo 'tipo'
    tipo_processo = [
        ("1 - Licenciamento", "Licenciamento"),
        ("2 - Denúncia", "Denúncia"),]
    tipo_status = [
        ("FE", "Está na fila de espera"),
        ("V", "À ser vistoriado"),
        ("A", "Em análise"),
        ("C", "Concluído"),
        ("Ar", "Arquivado"),
    ]

    # Campos do Formulário
    nome_solicitante = models.CharField(max_length=255, default= 'Nome não fornecido')
    rua = models.CharField(max_length=255)
    numero_casa = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=tipo_processo)
    descricao = models.TextField()

    # Campos Controle
    data_criacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=tipo_status)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    data_conclusao = models.DateField(null=True, blank=True)

    # Para representar o objeto como uma String, para dizer o andamento do processo administrativo  

    def __str__(self):
        return f"Protocolo: {self.protocolo} - Tipo: {self.tipo} - Status: {self.status}"