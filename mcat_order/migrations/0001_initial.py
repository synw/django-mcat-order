# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 12:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mcat', '0002_auto_20170529_1213'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Edited')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Published'), (1, 'Pending'), (2, 'Unpublished')], default=0, verbose_name='Status')),
                ('first_name', models.CharField(max_length=120, verbose_name='First name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Last name')),
                ('civility', models.CharField(choices=[('mr', 'Mr'), ('mm', 'Mme')], default='mr', max_length=60, verbose_name='Title')),
                ('telephone', models.PositiveIntegerField(verbose_name='Phone number')),
                ('company_name', models.CharField(blank=True, max_length=120, verbose_name='Company name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('extra', jsonfield.fields.JSONField(blank=True, default=dict, verbose_name='Extra infos')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Edited by')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ('last_name',),
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Edited')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('closed', 'Closed'), ('rejected', 'Rejected')], default='pending', max_length=120, verbose_name='Status')),
                ('total', models.FloatField(blank=True, null=True, verbose_name='Total')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mcat_order.Customer', verbose_name='Customer')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Edited by')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Orders',
                'verbose_name': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited', models.DateTimeField(auto_now=True, verbose_name='Edited')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price_per_unit', models.FloatField(verbose_name='Price per unit')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Edited by')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mcat_order.Order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered', to='mcat.Product', verbose_name='Product')),
            ],
            options={
                'ordering': ('-created', 'order'),
                'verbose_name_plural': 'Ordered products',
                'verbose_name': 'Ordered product',
            },
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
