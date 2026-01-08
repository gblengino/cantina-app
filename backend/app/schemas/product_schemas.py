from marshmallow import Schema, fields, validate

# INPUT SCHEMAS

class ProductCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    price = fields.Decimal(required=True, as_string=True, places=2)
    stock = fields.Int(required=True, validate=validate.Range(min=0))

# OUTPUT SCHEMAS

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    price = fields.Decimal(as_string=True, places=2)
    stock = fields.Int()
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

class ProductMiniSchema(Schema):
    id = fields.Int()
    name = fields.Str()