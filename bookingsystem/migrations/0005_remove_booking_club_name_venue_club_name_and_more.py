# Generated by Django 4.2.6 on 2023-10-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0004_booking_club_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='club_name',
        ),
        migrations.AddField(
            model_name='venue',
            name='club_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
