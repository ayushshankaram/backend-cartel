# Generated by Django 4.2.6 on 2023-10-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0003_alter_venue_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='club_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
