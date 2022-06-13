from datetime import date, datetime
from ninja import Schema, ModelSchema
from players.models import Player
from ninja.orm import create_schema

PlayerSchema = create_schema(Player, fields=[
                             'identifier', 'first_name', 'last_name', 'team', 'position', 'image', 'created_at', 'updated_at'])


class NotFoundSchema(Schema):
    message: str

# TrackSchema = create_schema(Track, fields=['title', 'last_play', 'artist', 'duration'])

# #class TrackSchema(ModelSchema):
# #    class Config:
# #        model = Track
# #        model_fields = {'title', 'last_play', 'artist', 'duration'}
