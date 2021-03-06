# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cropping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_id', models.IntegerField()),
                ('c_year', models.DateTimeField()),
                ('c_area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_lat', models.FloatField()),
                ('P_long', models.FloatField()),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farm')),
            ],
        ),
        migrations.RenameModel(
            old_name='Households',
            new_name='Household',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
        migrations.RemoveField(
            model_name='farms',
            name='H_id',
        ),
        migrations.DeleteModel(
            name='Farms',
        ),
        migrations.AddField(
            model_name='farm',
            name='H_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Household'),
        ),
        migrations.AddField(
            model_name='cropping',
            name='F_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farm'),
        ),
        migrations.AddField(
            model_name='cropping',
            name='crop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Crop'),
        ),
    ]
