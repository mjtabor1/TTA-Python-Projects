# Generated by Django 2.0.7 on 2019-06-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
