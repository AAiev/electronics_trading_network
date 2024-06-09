# Generated by Django 5.0.6 on 2024-06-09 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradingLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('type', models.CharField(choices=[('FA', 'Завод'), ('RN', 'Розничная сеть'), ('IE', 'Индивидуальный предприниматель')], max_length=30, verbose_name='тип звена сети')),
                ('level', models.SmallIntegerField(verbose_name='уровень в иерархии поставок')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='улица')),
                ('house_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='номер дома')),
                ('arrear', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='задолженность перед поставщиком')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading_platform.tradinglink', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'торговое звено',
                'verbose_name_plural': 'торговые звенья',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('model', models.CharField(max_length=200, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('trading_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_platform.tradinglink', verbose_name='торговое звено')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]