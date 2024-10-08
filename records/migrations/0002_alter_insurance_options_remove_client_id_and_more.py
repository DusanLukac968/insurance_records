# Generated by Django 5.0.7 on 2024-07-22 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insurance',
            options={'verbose_name': 'Insurance', 'verbose_name_plural': 'Insurances'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='value',
        ),
        migrations.AddField(
            model_name='client',
            name='id_client',
            field=models.IntegerField(default=30300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='insurance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.insurance', verbose_name='Insurance'),
        ),
    ]
