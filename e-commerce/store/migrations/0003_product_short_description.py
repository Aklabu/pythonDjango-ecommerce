# Generated by Django 5.2.4 on 2025-07-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
