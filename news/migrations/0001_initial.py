# Generated by Django 2.2.5 on 2019-10-15 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2019, 10, 15, 10, 25, 57, 178648))),
            ],
        ),
    ]