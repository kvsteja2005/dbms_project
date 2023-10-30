# Generated by Django 4.2.6 on 2023-10-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('event_location', models.CharField(max_length=255)),
            ],
        ),
    ]