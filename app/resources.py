from flask_restx import Resource, Namespace 

from .api_models import product_model, item_model, product_input_model, item_input_model
from .extensions import db
from .models import product, item

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}

@ns.route("/products")
class productListAPI(Resource):
    @ns.marshal_list_with(product_model)
    def get(self):
        return product.query.all()

    @ns.expect(product_input_model)
    @ns.marshal_with(product_model)
    def post(self):
        product = product(name=ns.payload["name"])
        db.session.add(product)
        db.session.commit()
        return product, 201

@ns.route("/products/<int:id>")
class productAPI(Resource):
    @ns.marshal_with(product_model)
    def get(self, id):
        product = product.query.get(id)
        return product

    @ns.expect(product_input_model)
    @ns.marshal_with(product_model)
    def put(self, id):
        product = product.query.get(id)
        product.name = ns.payload["name"]
        db.session.commit()
        return product

    def delete(self, id):
        product = product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return {}, 204


@ns.route("/items")
class itemListAPI(Resource):
    @ns.marshal_list_with(item_model)
    def get(self):
        return item.query.all()

    @ns.expect(item_input_model)
    @ns.marshal_with(item_model)
    def post(self):
        item = item(name=ns.payload["name"], product_id=ns.payload["product_id"])
        db.session.add(item)
        db.session.commit()
        return item, 201


@ns.route("/items/<int:id>")
class itemAPI(Resource):
    @ns.marshal_with(item_model)
    def get(self, id):
        item = item.query.get(id)
        return item

    @ns.expect(item_input_model)
    @ns.marshal_with(item_model)
    def put(self, id):
        item = item.query.get(id)
        item.name = ns.payload["name"]
        item.product_id = ns.payload["product_id"]
        db.session.commit()
        return item

    def delete(self, id):
        item = item.query.get(id)
        db.session.delete(item)
        db.session.commit()
        return {}, 204