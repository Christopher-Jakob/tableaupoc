# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-13 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_firstname', models.CharField(max_length=100)),
                ('author_lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.IntegerField()),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='Store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Stores'),
        ),
    ]
