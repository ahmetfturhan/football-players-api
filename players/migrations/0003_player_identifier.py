# Generated by Django 4.0.5 on 2022-06-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_remove_player_created_at_remove_player_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='identifier',
            field=models.IntegerField(default=99999),
            preserve_default=False,
        ),
    ]
