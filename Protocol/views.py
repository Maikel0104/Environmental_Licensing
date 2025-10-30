from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import processo_administrativo
from .forms import ProcessoForm

# View 1: Menu Principal

@login_required # Garante que o usuário esteja autenticado para acessar esta view
def menu_principal(request):
    # Apenas renderiza o template do menu principal quando a view é acessada
    # Não dados adicionais são necessários aqui
    return render(request, 'Protocol/tela_home.html')


# View 2: Histórico de Licenças

@login_required
def historico_licencas(request):
    # Busca as licenças associadas ao usuário autenticado e as envia para o template
    
    # Filtrando as licenças pelo usuário logado
    lista_de_licencas = processo_administrativo.objects.filter(
        user_fk=request.user,
        tipo="1 - Licenciamento"
        ).order_by('-data_criacao') # Mais recentes primeiro

    context = {
        'lista_de_licencas': lista_de_licencas
    }

    return render(request, 'Protocol/tela_historico_licenca.html', context)

# View 3: Histórico de denúncias
@login_required
def historico_denuncias(request):
    # Busca as denúncias do usuário logado e as envia para o template

    lista_de_denuncias = processo_administrativo.objects.filter(
        user_fk=request.user,
        tipo="2 - Denúncia"
    ).order_by('-data_criacao') # Mais recentes primeiro

    context = {
        'lista_de_denuncias': lista_de_denuncias
    }
    return render(request, 'Protocol/tela_historico_denuncias.html', context)


# View 4: Novo Pedido de Denúncia
@login_required
def novo_pedido(request):
    # Esta view faz duas coisas:
    # 1. (GET) Mostra um formulário em branco.
    # 2. (POST) Processa os dados do formulário quando o usuário o envia

    if request.method == 'POST':
        # O usuário está SUBMETENDO o formulário 
        form = ProcessoForm(request.POST)

        if form.is_valid():
            # formulário é válido!
            # commit=False: Não salvar ainda no banco de dados
            # Vamos adicionar o usuário antes de salvar
            novo_processo = form.save(commit=False)
            novo_processo.user_fk = request.user # Atribui o usuário logado à denúncia
            novo_processo.status = 'FE' # Define o status inicial como 'FILA DE ESPERA'
            novo_processo.save() # Agora salva no banco de dados

            # Mágica do Bootstrap/Django para mensagens de sucesso
            messages.success(request, 'Seu pedido foi registrado com sucesso!')

            if novo_processo.tipo == '1 - Licenciamento':
                return redirect('historico_licencas')
            else:
                return redirect('historico_denuncias')
            # Redireciona o usuário para a página de histórico de denúncias
        else:
            # O formulário é inválido, o Django vai reenviar o 'form' para o template com as mensagens de erro.
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        # O usuário está ACESSANDO o formulário pela primeira vez (GET)
        form = ProcessoForm() # Cria um formulário em branco

    # Envia o formulário (em branco ou com erros) para o template
    context = {
        'form': form
    }
    return render(request, 'Protocol/tela_novo_pedido.html', context)
