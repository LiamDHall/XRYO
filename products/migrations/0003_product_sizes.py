# Generated by Django 3.1.7 on 2021-03-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210324_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
