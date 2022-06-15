from datetime import date, datetime
import uuid
from ninja import Schema, Field, ModelSchema
from players.models import Player
from ninja.orm import create_schema


PlayerInSchema = create_schema(Player, fields=[
    'identifier', 'first_name', 'last_name', 'team', 'position', 'image'])

PlayerOutSchema = create_schema(Player, fields=[
    'identifier', 'first_name', 'last_name', 'team', 'position', 'image', 'created_at', 'updated_at'])

# class PlayerInSchema(Schema):
#     identifier: int = Field(required=True)
#     first_name: str = Field(required=True)
#     last_name: str = Field(required=True)
#     team: str = Field(required=True)
#     position: str = Field(required=True)
#     image: str = Field(required=True)

# class PlayerOutSchema(PlayerInSchema):
#     id: uuid.UUID = Field(required=True)
#     created_at: datetime.now = Field(auto_now_add=True, required=False)
#     updated_at: datetime.now = Field(auto_now=True, required=False)


# If the player does not exist in database

class NotFoundSchema(Schema):
    message: str
