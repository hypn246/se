from saleapp import db, app, model
from saleapp.model import Category, Product


def load_categories():
    # with open("data/category.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()

def load_products(q=None, cate_id=None, pg=None):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     if q:
    #         products = [p for p in products if p["name"].find(q)>=0]
    #
    #     if cate_id:
    #         products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]
    #
    #     return products
    query=Product.query
    if(q):
        query=query.filter(Product.name.contains(q))
    if (cate_id):
        query=query.filter(Product.cate_id.__eq__(cate_id))
    if (pg):
        query=query.filter(Product.offset(pg*1).limit(pg*3+3).all())
    return query.all()

def count_prod():
    return Product.query.count()

def get_product_by_id(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     for p in products:
    #         if p["id"].__eq__(id):
    #             return p
    #
    # return None
    return Product.query.get(id)

if __name__=="__main__":
    print(get_product_by_id(1))
