# Generated by Django 2.2.4 on 2020-10-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to='foto_perfil/'),
        ),
    ]