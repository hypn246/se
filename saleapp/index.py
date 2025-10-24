import json
import math

from flask import Flask, render_template, request
import dao
from saleapp import db, app
# app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    pg= request.args.get("page")
    prods = dao.load_products(q=q, cate_id=cate_id, pg=pg)
    pages=math.ceil(dao.count_prod()/3)
    return render_template("index.html", prods=prods, pages=pages)

@app.route("/products/<int:id>")
def details(id):
    prod = dao.get_product_by_id(id)
    return render_template("product-details.html", prod=prod)

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)