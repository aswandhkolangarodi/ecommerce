from django.urls import path
from . import views

app_name = "products"

urlpatterns = [

    path('list/category',views.CategoryListView.as_view(), name='list_category'),
    path('list/sub_category',views.SubCategoryListView.as_view(), name='list_sub_category'),
    path('list/product',views.ProductListView.as_view(), name='list_product'),
]
