# Generated by Django 5.1.6 on 2025-02-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_alter_filmes_options_alter_filmes_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]
