# Generated by Django 3.2.17 on 2023-02-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'company',
                'db_table': 'Basic_company',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='岗位名称')),
                ('Personal_name', models.CharField(max_length=100, unique=True, verbose_name='人员姓名')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basicweb.company', verbose_name='所属部门')),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Major',
                'db_table': 'Basic_Major',
                'managed': True,
            },
        ),
    ]