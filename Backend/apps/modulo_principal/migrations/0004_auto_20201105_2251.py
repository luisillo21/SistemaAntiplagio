# Generated by Django 2.2.4 on 2020-11-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_principal', '0003_auto_20201104_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=50),
        ),
    ]