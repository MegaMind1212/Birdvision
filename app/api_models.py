from flask_restx import fields

from .extensions import api 

item_model = api.model("item", {
    "id": fields.Integer,
    "name": fields.String,
    #"product": fields.Nested(product_model)
})

product_model = api.model("product", {
    "id": fields.Integer,
    "name": fields.String,
    "items": fields.List(fields.Nested(item_model))
})

product_input_model = api.model("productInput", {
    "name": fields.String,
})

item_input_model = api.model("itemInput", {
    "name": fields.String,
    "product_id": fields.Integer
})