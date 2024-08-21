# Generated by Django 5.0.7 on 2024-08-16 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_insurance_insurance_value_alter_user_insurance_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='insurance_value',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
