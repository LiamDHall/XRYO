# Generated by Django 3.1.7 on 2021-04-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
