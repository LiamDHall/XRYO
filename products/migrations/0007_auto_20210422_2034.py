# Generated by Django 3.1.7 on 2021-04-22 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210421_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.imagealbum'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='variant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
