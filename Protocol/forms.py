from django import forms
from .models import processo_administrativo # Importe seu modelo de denúncia

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = processo_administrativo
        # Liste os campos do modelo que o formulário deve mostrar
        # O django vai gerar automaticamente os campos do formulário com base no modelo
        fields = ['nome_solicitante', 
                  'rua', 
                  'numero_casa', 
                  'bairro', 
                  'cidade', 
                  'tipo', 
                  'descricao'
                  ]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Este loop adiciona a classe 'form-control' do Bootstrap a todos os campos do formulário
        for field_name, field in self.fields.items():
            #  O 'tipo' deve ser um <select>
            field.widget.attrs['class'] = 'form-control'
        
        #Renomeia os labels
        self.fields['nome_solicitante'].label = 'Nome'
        self.fields['numero_casa'].label = 'Nº Casa'
