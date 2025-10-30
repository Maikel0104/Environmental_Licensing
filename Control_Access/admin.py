from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'CNPJ', 'data_nascimento', 'telefone', 'rua', 'numero_casa', 'bairro', 'cidade')
    search_fields = ('user__username', 'cpf', 'CNPJ')
    list_filter = ('data_nascimento',)
    
    
#@admin.register(processo_administrativo)
#class ProcessoAdministrativoAdmin(admin.ModelAdmin):
#    list_display = ('protocolo', 'tipo', 'status', 'data_criacao', 'data_conclusao', 'user_fk', 'rua', 'numero_casa', 'bairro', 'cidade')
#    search_fields = ('protocolo', 'user_fk__username', 'status')
#    list_filter = ('tipo', 'status', 'data_criacao')
    