# Generated by Django 4.2 on 2024-09-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/product_images/제목_없는_아트워크_82.png', upload_to='product_images/'),
        ),
    ]
