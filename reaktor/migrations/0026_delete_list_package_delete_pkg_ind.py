# Generated by Django 4.0.4 on 2022-05-29 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reaktor', '0025_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List_package',
        ),
        migrations.DeleteModel(
            name='Pkg_Ind',
        ),
    ]