# Generated by Django 4.1.2 on 2022-10-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_followedevent_event_seatgeek_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='followedevent',
            name='event_image',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
