from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class HomeView(ListView):
    model = Product
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['is_index'] = True
        return context