# Generated by Django 3.2.8 on 2022-07-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('create', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
