from django.contrib import admin
from .models import Category, SubCategory, Product


class SubCategoryInline(admin.TabularInline):  
    model = SubCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", )
    search_fields = ("category_name",)  
    inlines = [SubCategoryInline]  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sub_category","product_name","price")