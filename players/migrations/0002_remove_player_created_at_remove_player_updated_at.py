# Generated by Django 4.0.5 on 2022-06-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='player',
            name='updated_at',
        ),
    ]
