# Generated by Django 4.0.5 on 2022-06-15 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_player_created_at_player_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Player',
            new_name='PlayerIn',
        ),
    ]
