# Generated by Django 3.0.6 on 2020-05-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20200530_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='code',
            field=models.TextField(blank=True),
        ),
    ]