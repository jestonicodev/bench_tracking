# Generated by Django 4.2.11 on 2024-04-05 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0004_user_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temporary_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]