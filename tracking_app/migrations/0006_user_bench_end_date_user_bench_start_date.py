# Generated by Django 4.2.11 on 2024-04-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0005_user_temporary_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bench_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bench_start_date',
            field=models.DateField(null=True),
        ),
    ]