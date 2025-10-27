# /app/Controle_Acesso/forms.py

# Importa o módulo de formulários do Django
from django import forms

# Importa o formulário de criação de usuário padrão do Django
from django.contrib.auth.forms import UserCreationForm

# Importa o modelo de usuário padrão do Django
from django.contrib.auth.models import User

from .models import Usuario

# Aqui estou implementando as funcionalidades de formulário de login
from django.contrib.auth.forms import AuthenticationForm

# Aqui estou implementando as funcionalidades do formulário de reset de senha
from django.contrib.auth.forms import PasswordResetForm

# Formulário 1: Para criar o User (username, email, senha) (com estilo bootstrap)
# Este herda do UserCreationForm para garantir a segurança da senha

class FormularioCadastro(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail') # Campo de email obrigatório
    nome_completo = forms.CharField(label='Nome Completo', max_length=150, required=True) # Campo de nome completo obrigatório
    # Usei a classe meta para definir o comportamento e a organização do formulário
    

    def __init__(self, *args, **kwargs):
        super(FormularioCadastro, self).__init__(*args, **kwargs)

        # Adicionando classes e placeholders para cada campo
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': 'Nome de Usuário'}
            )
        self.fields['nome_completo'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': 'Insira seu nome completo'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control border-success', 'id':'id_email', 'placeholder': 'Insira seu email'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': 'Digite sua senha'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': 'Confirme sua senha'}
        )

        # Alterando os labels para ficarem mais amigáveis
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de Senha"
        
    class Meta(UserCreationForm.Meta):
        # o UserCreationForm já sabe que o model é User
        # e que os campos padrão são username e os de senha.
        pass
    

# Formulário 2: Para criar o Administrador
class FormularioAdministrador(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(FormularioAdministrador, self).__init__(*args, **kwargs)
        # Adicionando classes e placeholders para cada campo do formulário
        self.fields['cpf'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': '___.____.____-__'}
        )

        self.fields['data_nascimento'].widget.attrs.update(
            {'class': 'form-control border-success'}
        )

    class Meta:
        model = Usuario
        fields = ['cpf', 'data_nascimento'] # Campos para o Administrador
        labels = {
            'cpf': 'CPF',
            'data_nascimento': 'Data de Nascimento',
        }
        # Widget para facilitar a inserção de data
        widgets = {
            # attrs define atributos HTML do tipo date para renderizar um calendário no template html
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}), 
        }

# Formulário 3: Criar uma classe para complementar o LoginView
class FormularioLogin (AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Nome de Usuário'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Senha'}
        )

#Formulário 4: Criar uma classe complementar o campo de email da tela 'email_recuperacao'
class FormularioResetSenha(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(FormularioResetSenha, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Digite seu Email de Cadastro'}
        )