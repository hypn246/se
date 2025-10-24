import json

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import  relationship

from saleapp import db, app

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.name

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)

class Product(Base):
    price = Column(Float, default=0.0)
    image = Column(String(400),
                   default="https://res.cloudinary.com/dy1unykph/image/upload/v1740037805/apple-iphone-16-pro-natural-titanium_lcnlu2.webp")
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        c1 = Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        with open("data/product.json", encoding='utf-8') as f:
            ps=json.load(f)
            for p in ps:
                db.session.add(Product(**p))
        db.session.commit()