# Generated by Django 4.0.4 on 2022-05-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reaktor', '0010_delete_list_package_delete_pkg_ind'),
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
                ('depend_name', models.CharField(max_length=500)),
                ('depend_version', models.CharField(max_length=100)),
                ('pack_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reaktor.list_package')),
            ],
            options={
                'db_table': 'pkg_ind',
            },
        ),
    ]