from marshmallow import Schema, fields

# OUTPUT SCHEMAS

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    role = fields.Str(attribute="credential.role", dump_only=True)
    is_active = fields.Bool(dump_only=True)

class UserResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(dump_only=True)
    role = fields.Str(attribute="credential.role", dump_only=True)

class UserCredentialSchema(Schema):
    id = fields.Int(dump_only=True)
    role = fields.Str(dump_only=True)
    user_id = fields.Int(dump_only=True)
    user = fields.Nested("UserSchema", only=("id", "username"), dump_only=True)