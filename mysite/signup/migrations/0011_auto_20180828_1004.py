# Generated by Django 2.0.7 on 2018-08-28 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0010_auto_20180828_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_receive',
            new_name='is_email',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='sms_receive',
            new_name='is_sms',
        ),
    ]
