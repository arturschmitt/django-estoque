# Generated by Django 4.1.3 on 2022-11-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('quantidade', models.PositiveIntegerField()),
                ('descricao', models.CharField(max_length=180)),
            ],
        ),
    ]
