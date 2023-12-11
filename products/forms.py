from django import forms
from .models import Product

class ProdutcForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('nome', 'descricao', 'preco', 'validade')
        template_name = 'create_post.html'