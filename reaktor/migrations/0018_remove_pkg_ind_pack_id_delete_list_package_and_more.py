# Generated by Django 4.0.4 on 2022-05-28 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reaktor', '0017_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pkg_ind',
            name='pack_id',
        ),
        migrations.DeleteModel(
            name='List_package',
        ),
        migrations.DeleteModel(
            name='Pkg_Ind',
        ),
    ]