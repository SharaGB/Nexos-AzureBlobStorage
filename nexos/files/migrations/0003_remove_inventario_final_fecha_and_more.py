# Generated by Django 4.1 on 2022-08-08 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_files_remove_gln_cliente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario_final',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='inventario_final',
            name='hora',
        ),
    ]