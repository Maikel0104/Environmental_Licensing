from django.shortcuts import render, redirect
from .forms import FormularioCadastro # Importe o formulário de criação de usuário
from .forms import FormularioAdministrador # Importe o formulário de criação do administrador 
from django.db import transaction # Importa transaction para garantir que ambos os formulários sejam salvos juntos

# transaction.atomic garante que ambas as operações de salvamento sejam atômicas
@transaction.atomic
def view_cadastro(request):
    if request.method == 'POST':
        # Se o formulário foi enviado (MÉTODO POST)
        form1 = FormularioCadastro(request.POST)
        form2 = FormularioAdministrador(request.POST)
        if form1.is_valid() and form2.is_valid():
            # 1. Salve o primeiro formulário e obtenha o objeto User
            user = form1.save() # Salva o novo usuário no banco de dados
            # 2. Salve o segundo formulário, mas não confirme ainda (commit=False)
            perfil = form2.save(commit=False)
            # 3. Associe o objeto User ao perfil de Administrador
            perfil.user = user
            # 4. Agora salve o perfil de Administrador no banco de dados
            perfil.save()
            # 5. Redirecione para a página de login
            return redirect('login') # Redireciona para a página de login
    else:
        # Se a página foi apenas acessada (MÉTODO GET)
        form1 = FormularioCadastro()
        form2 = FormularioAdministrador()
    
    # Renderiza o template, passando o formulário como contexto
    context = {
        'form1' : form1,
        'form2' : form2
    }
    return render(request, 'Control_Access/Cadastrar_Conta.html', context)