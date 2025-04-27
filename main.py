from fastapi import FastAPI

from indb import generate_products
from json_db import JsonDB
from product import Product

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
  products = productDB.read()
  return { "products": products }

@app.post('/products')
def create_product(product: Product):

  productDB.insert(product)
  return { "status": "inserted" }