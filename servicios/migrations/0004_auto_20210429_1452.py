# Generated by Django 3.1.7 on 2021-04-29 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_remove_reporte_descripcionsolucion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otrosingresos',
            old_name='idClienteFk',
            new_name='idClienteFK',
        ),
    ]