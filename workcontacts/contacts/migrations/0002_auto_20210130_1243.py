# Generated by Django 2.2 on 2021-01-30 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(max_length=30, unique=True, verbose_name='Уникальное имя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='contacts.Company', verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='second_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Вид связи')),
                ('value', models.CharField(max_length=200, verbose_name='Номер')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='contacts.Employee', verbose_name='Сотрудник')),
            ],
        ),
    ]
