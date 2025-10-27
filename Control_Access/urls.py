# Controle_Acesso/urls.py

# Importa a função 'path' do Django para criar as rotas
# e o arquivo 'views.py' do mesmo diretório (app)
from django.urls import path
from . import views
from .forms import FormularioLogin # Importa o formulário de login 
from .forms import FormularioResetSenha

# Aqui importa as views de autenticação do Django
from django.contrib.auth import views as auth_views

# Esta é a lista onde todas as rotas (URLs) do seu app são definidas
urlpatterns = [
    # Rota 1: Cadastro
    path('cadastro/', views.view_cadastro, name='cadastro'),
    # Rota 2: Login
    # Usamos a LoginView pronta do Django para facilitar o processo de criação do login
    # Portanto, não precisamos criar uma view personalizada para o login
    path('login/', auth_views.LoginView.as_view(
        template_name='Control_Access/login2.html', # Aponta para o template de login
        authentication_form=FormularioLogin
    ), name='login'),
    # Rota 3: Logout
    #path('logout/', views.view_logout, name='logout'),

    # ROTAS PARA RECUPERAÇÃO DE SENHA

    # 1. Página para pedir a redefinição (onde o usuário digita o email)
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='Control_Access/Email_Recuperacao.html', form_class=FormularioResetSenha),
         name='password_reset'),
    # 2. Página de sucesso após o pedido (avisando que o email foi enviado)
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='Control_Access/password_reset_done.html'),
         name='password_reset_done'),
    # 3. O link que o usuário recebe no email (com token) para criar a nova senha
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='Control_Access/Senha_Recuperacao.html'),
         name='password_reset_confirm'),
    # 4. Página de sucesso após a senha ser trocada
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='Control_Access/password_reset_complete.html'),
         name='password_reset_complete'),
]