from django.shortcuts import render, redirect
from .forms import FormularioCadastro # Importe o formulário de criação de usuário
from .forms import UsuarioForm 
from .forms import FormularioLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
# Importe o formulário de criação do administrador 
from django.db import transaction # Importa transaction para garantir que ambos os formulários sejam salvos juntos

@transaction.atomic # Garante que ambas as operações de salvamento sejam atômicas
def view_cadastro(request):
    if request.method == 'POST':
        # Se o formulário foi enviado (MÉTODO POST)
        user_form = FormularioCadastro(request.POST)
        profile_form = UsuarioForm(request.POST)
        
        # 1. VERIFICA SE OS DOIS FORMULÁRIOS SÃO VÁLIDOS
        if user_form.is_valid() and profile_form.is_valid():
            # 2. Salve primeiro o user e obtenha o objeto User
            
            # Método save já cuida de criptografar a senha
            user = user_form.save()

            # 3. CRIE O PERFIL "EM MEMÓRIA" SEM SALVAR AINDA"
            profile = profile_form.save(commit=False)

            # 4. CONECTA O PERFIL AO USUÁRIO CRIADO
            profile.user = user

            # 5. AGORA SALVE O PERFIL NO BANCO DE DADOS
            profile.save()

            # Loga o usuário automaticamente após o cadastro
            login(request, user) 
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('menu_principal')  # Redireciona para a página inicial após o cadastro
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados inseridos.')

    else:
        # Se a página foi apenas acessada (MÉTODO GET), crie dois formulários vazios
        user_form = FormularioCadastro()
        profile_form = UsuarioForm()
        
    
    # 6. ENVIE OS DOIS FORMULÁRIOS PARA O TEMPLATE
    context = {
        'user_form' : user_form,
        'profile_form': profile_form
    }
    return render(request, 'Control_Access/Cadastrar_Conta.html', context)      