from .extensions import db 

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    items = db.relationship("item", back_populates="product")


class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    product_id = db.Column(db.ForeignKey("product.id"))

    product = db.relationship("product", back_populates="items")