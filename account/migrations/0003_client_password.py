# Generated by Django 3.2.9 on 2021-11-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211127_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='null', max_length=40),
        ),
    ]