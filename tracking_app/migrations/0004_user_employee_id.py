# Generated by Django 4.2.11 on 2024-04-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_app', '0003_user_is_bench_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]