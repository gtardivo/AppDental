# Generated by Django 4.1.4 on 2022-12-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=20)),
                ('cel', models.CharField(max_length=20)),
            ],
        ),
    ]
