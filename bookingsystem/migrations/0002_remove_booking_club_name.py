# Generated by Django 4.2.6 on 2023-10-28 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='club_name',
        ),
    ]
