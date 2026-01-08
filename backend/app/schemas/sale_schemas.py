from marshmallow import Schema, fields, validate
from schemas.product_schemas import ProductMiniSchema

# INPUT SCHEMAS

class SaleItemCreateSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

class SaleCreateSchema(Schema):
    cash_register_id = fields.Int(required=True)
    items = fields.List(
        fields.Nested(SaleItemCreateSchema),
        required=True,
        validate=validate.Length(min=1)
    )

# OUTPUT SCHEMAS

class SaleItemSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Nested(ProductMiniSchema)
    quantity = fields.Int()
    unit_price = fields.Decimal(as_string=True, places=2)
    subtotal = fields.Decimal(as_string=True, places=2)

class SaleSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    cash_register_id = fields.Int(dump_only=True)
    total = fields.Decimal(as_string=True, places=2, dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    items = fields.List(
        fields.Nested(SaleItemSchema),
        dump_only=True
    )