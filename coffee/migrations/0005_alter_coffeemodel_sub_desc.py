# Generated by Django 5.2.1 on 2025-06-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_coffeemodel_sub_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeemodel',
            name='sub_desc',
            field=models.CharField(max_length=200, verbose_name='qisqa komment'),
        ),
    ]
