from datetime import date, datetime
from ninja import Schema, ModelSchema
from players.models import Player
from ninja.orm import create_schema


PlayerSchema = create_schema(Player, fields=[
                             'identifier', 'first_name', 'last_name', 'team', 'position', 'image', 'created_at', 'updated_at'])

# If the player does not exist in database
class NotFoundSchema(Schema):
    message: str
