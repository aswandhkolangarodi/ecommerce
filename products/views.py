from django.shortcuts import render
from django.views.generic import ListView

from products.models import Category, Product, SubCategory


class CategoryListView(ListView):
    model = Category

class SubCategoryListView(ListView):
    model = SubCategory

class ProductListView(ListView):
    model = Product