# Generated by Django 4.0.4 on 2022-05-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaktor', '0002_list_package_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pkg_Ind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depend_name', models.CharField(max_length=500)),
                ('depend_version', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pkg_ind',
            },
        ),
    ]
