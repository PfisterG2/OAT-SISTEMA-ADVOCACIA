# Generated by Django 5.1.3 on 2024-11-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advogado',
            name='email',
        ),
        migrations.AlterField(
            model_name='advogado',
            name='especializacao',
            field=models.CharField(default='Não especificado', max_length=255),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='oab',
            field=models.CharField(max_length=20),
        ),
    ]
