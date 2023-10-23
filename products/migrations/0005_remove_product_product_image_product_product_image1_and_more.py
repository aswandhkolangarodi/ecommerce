# Generated by Django 4.2.5 on 2023-10-23 07:13

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=versatileimagefield.fields.VersatileImageField(default=1, upload_to='products/', verbose_name='Product_Image1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=versatileimagefield.fields.VersatileImageField(default=1, upload_to='products/', verbose_name='Product_Image2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Product_Image2 PPOI'),
        ),
    ]