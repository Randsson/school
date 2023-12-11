from django.shortcuts import render
from .models import Product
from django.views.generic import CreateView
from .forms import ProdutcForm

class ProductCreateView(CreateView):
    form_class = ProdutcForm
    template_name = 'create_post.html'
    success_url = '/'