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

        # 1. Esconde o campo 'username' padrão do UserCreationForm
        self.fields['username'].widget = forms.HiddenInput()
        # 2. Torna o 'username' não obrigatório (já que vamos usar o email como username)
        self.fields['username'].required = False

        
        # Estilizando os campos que o usuário vai ver no formulário
        # Adicionando classes e placeholders para cada campo do formulário
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
        model = User
        fields = ('username', 'email')
    
    def clean_email(self):
        # O email é usado como username, então precisa ser único
        email = self.cleaned_data['email']
        if User.objects.filter(username__iexact=email).exists() or User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Já existe uma conta cadastrada com este e-mail.')
        return email

    def save(self, commit=True):
        # Primeiro, salva o usuário com username e senha (criptografada)
        user = super(FormularioCadastro, self).save(commit=False)

        # Agora, pegue os dados extras do formulário limpo
        user.username = self.cleaned_data['email']  # Usando o email como username
        user.email = self.cleaned_data['email']

        # o 'User' não têm 'nome_completo', mas tem 'first_name' e 'last_name'
        nome_completo = self.cleaned_data['nome_completo']
        user.first_name = nome_completo.split(' ')[0]  # Primeiro nome
        user.last_name = ' '.join(nome_completo.split(' ')[1:])  #

        if commit:
            user.save()  # Salva o usuário no banco de dados
        
        return user
    

# Formulário 2: Para criar o perfil de usuário (cpf, data_nascimento) (com estilo bootstrap)
class UsuarioForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        # Aceita o CPF com pontuação (até 14 caracteres); o clean_cpf deixa só os 11 dígitos
        self.fields['cpf'].max_length = 14
        self.fields['cpf'].validators = []

        # Adicionando classes e placeholders para cada campo do formulário
        self.fields['cpf'].widget.attrs.update(
            {'class': 'form-control border-success', 'placeholder': '000.000.000-00', 'maxlength': '14'}
        )

        self.fields['data_nascimento'].widget.attrs.update(
            {'class': 'form-control border-success'}
        )
        # (Adicione aqui os outros campos do seu modelo 'Usuario', 
        # como 'telefone', 'rua', etc., se você os quiser no formulário de cadastro)

    def clean_cpf(self):
        # Remove pontos e traço e garante que o CPF tenha 11 dígitos
        cpf = self.cleaned_data.get('cpf')
        if not cpf:
            return None
        cpf = ''.join(c for c in cpf if c.isdigit())
        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve conter 11 dígitos.')
        if Usuario.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Já existe uma conta cadastrada com este CPF.')
        return cpf

    class Meta:
        model = Usuario
        fields = ['cpf', 'data_nascimento']
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
        
        # 1. Muda o label de "Username" para "E-mail"
        self.fields['username'].label = 'E-mail'
        # 2. Muda o placeholder e adiciona a classe bootstrap
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'seu@email.com'}
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