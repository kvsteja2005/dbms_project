# Generated by Django 4.2.7 on 2023-11-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_event_host_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='host_details',
            field=models.TextField(default='Tell about yourself'),
        ),
    ]
