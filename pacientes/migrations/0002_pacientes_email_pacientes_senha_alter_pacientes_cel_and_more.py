# Generated by Django 4.1.4 on 2022-12-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pacientes",
            name="email",
            field=models.CharField(default=" ", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pacientes",
            name="senha",
            field=models.CharField(default=" ", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pacientes",
            name="cel",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="pacientes",
            name="cpf",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="pacientes",
            name="endereco",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="pacientes",
            name="nome",
            field=models.CharField(max_length=100),
        ),
    ]
