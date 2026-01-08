from marshmallow import Schema, fields, validate
from app.constants.roles import Roles
from schemas.user_schemas import UserResponseSchema

# INPUT SCHEMAS

class RegisterSchema(Schema):
    username = fields.Str(
        required=True,
        validate=validate.Length(min=5,max=20)
        )
    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=8)
        )
    role = fields.Str(
        load_only=True,
        validate=validate.OneOf(Roles.values())
        )

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

# OUTPUT SCHEMAS

class AuthResponseSchema(Schema):
    access_token = fields.Str(dump_only=True)
    user = fields.Nested(UserResponseSchema, dump_only=True)