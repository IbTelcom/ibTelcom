# Generated by Django 3.1.7 on 2021-05-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_auto_20210508_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numeroTelefonoDos',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]