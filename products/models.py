from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField

class Category(models.Model):
    category_name = models.CharField(max_length=128)
    category_image = VersatileImageField('Category Image',upload_to="category/")
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
    price =models.DecimalField(max_digits=10, decimal_places=2)
    product_image1 = VersatileImageField('Product_Image1',upload_to="products/")
    ppoi = PPOIField("Product_Image1 PPOI")
    product_image2 = VersatileImageField('Product_Image2',upload_to="products/")
    ppoi = PPOIField("Product_Image2 PPOI")
    product_description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['sub_category','product_name']

    def __str__(self):
        return self.product_name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_variants')
    variant_name = models.CharField(max_length=150)
    variant_description = models.TextField(null=True, blank=True)

class ProductImage(models.Model):
    product_varient = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name='product_images')
    product_image = VersatileImageField('Product_Image',upload_to="category/")
    ppoi = PPOIField("Product_Image PPOI")

