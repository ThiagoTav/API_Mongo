# Generated by Django 4.1.13 on 2024-03-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('date', models.DateTimeField()),
                ('city', models.CharField(max_length=255)),
                ('atmosphericPressure', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('weather', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
