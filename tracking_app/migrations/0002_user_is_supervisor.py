# Generated by Django 4.2.11 on 2024-04-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_supervisor',
            field=models.BooleanField(default=False),
        ),
    ]