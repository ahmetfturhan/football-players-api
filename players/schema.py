from datetime import date, datetime
import uuid
from ninja import Schema, Field, ModelSchema
from players.models import Player
from ninja.orm import create_schema


PlayerInSchema = create_schema(Player, fields=[
    'identifier', 'first_name', 'last_name', 'team', 'position', 'image'])

PlayerOutSchema = create_schema(Player, fields=[
    'identifier', 'first_name', 'last_name', 'team', 'position', 'image', 'created_at', 'updated_at'])


# If the player does not exist in database

class NotFoundSchema(Schema):
    message: str
