from marshmallow import Schema, fields
from marshmallow import ValidationError

class ProductSchema(Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

def deserialize_product_json(json_data):
    product_schema = ProductSchema()
    try:
        product_data = product_schema.loads(json_data)
        return product_data
    except ValidationError as e:
        return {"error": str(e)}
