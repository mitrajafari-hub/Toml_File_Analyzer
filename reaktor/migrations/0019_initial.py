# Generated by Django 4.0.4 on 2022-05-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reaktor', '0018_remove_pkg_ind_pack_id_delete_list_package_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pdesc', models.CharField(max_length=700)),
            ],
            options={
                'db_table': 'list_package',
            },
        ),
        migrations.CreateModel(
            name='Pkg_Ind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_id', models.CharField(max_length=10)),
                ('depend_name', models.CharField(max_length=500)),
                ('depend_version', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pkg_ind',
            },
        ),
    ]
