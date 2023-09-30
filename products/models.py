from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    parent_category =models.ForeignKey('products.Category', on_delete=models.PROTECT)
    sub_category_name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'
        ordering = ['parent_category','sub_category_name']

    def __str__(self):
        return f"{self.sub_category_name} {self.parent_category} "
    
class Product(models.Model):
    sub_category = models.ForeignKey('products.SubCategory',on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    price =models.DecimalField(max_digits=5, decimal_places=2)
    product_description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['sub_category','product_name']

    def __str__(self):
        return self.product_name
        


