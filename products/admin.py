from django.contrib import admin
from .models import Category, SubCategory, Product, ProductVariant, ProductImage



class SubCategoryInline(admin.TabularInline):  
    model = SubCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", )
    search_fields = ("category_name",)  
    inlines = [SubCategoryInline]  

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sub_category","product_name","price")
    inlines = [ProductVariantInline]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product","variant_name")
    inlines = [ProductImageInline]