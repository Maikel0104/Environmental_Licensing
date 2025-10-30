from django.shortcuts import render, redirect
from .forms import FormularioCadastro # Importe o formulário de criação de usuário
from .forms import FormularioAdministrador
from .forms import FormularioLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
# Importe o formulário de criação do administrador 
from django.db import transaction # Importa transaction para garantir que ambos os formulários sejam salvos juntos

# transaction.atomic garante que ambas as operações de salvamento sejam atômicas
@transaction.atomic
def view_cadastro(request):
    if request.method == 'POST':
        # Se o formulário foi enviado (MÉTODO POST)
        user_form = FormularioCadastro(request.POST)
        profile_form = FormularioAdministrador(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # 1. Salve o primeiro formulário e obtenha o objeto User
            # Método save já cuida de criptografar a senha
            user = user_form.save()


            # 2. Salve o segundo formulário, mas não confirme ainda (commit=False)
            profile = profile_form.save(commit=False)
            # 3. Associe o objeto User ao perfil de Administrador
            profile.user = user
            # 4. Agora salve o perfil de Administrador no banco de dados
            profile.save()

            # Loga o usuário automaticamente após o cadastro
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('menu_principal')  # Redireciona para a página inicial após o cadastro
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados inseridos.')

    else:
        # Se a página foi apenas acessada (MÉTODO GET)
        user_form = FormularioCadastro()
        profile_form = FormularioAdministrador()
    
    # Renderiza o template, passando o formulário como contexto
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'Control_Access/Cadastrar_Conta.html', context)

def login_view(request):
    if request.method == 'POST':
        # Use o formulário customizado para autenticação
        form = FormularioLogin(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Autentica o usuário
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'Bem-vindo, {user.first_name}.')
                return redirect('menu_principal') # Redireciona para a página inicial após o login
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = FormularioLogin()
    
    # Renderiza o template, passando o formulário como contexto
    return render(request, 'Control_Access/login.html', {'form': form})
        