# Generated by Django 3.2.9 on 2021-11-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('email',
                 models.EmailField(default='null@example.com',
                                   max_length=254,
                                   primary_key=True,
                                   serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('email',
                 models.EmailField(default='null@example.com',
                                   max_length=254,
                                   primary_key=True,
                                   serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('cellNumber', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
                ('dateOfBirth', models.DateField(null=True)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email',
                 models.EmailField(default='null@example.com',
                                   max_length=254,
                                   primary_key=True,
                                   serialize=False)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
