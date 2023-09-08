from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/')
db=client.student

product=db.Product

product.insert_one({"PROD ID":1,"PRODUCT NAME":"SHAMPOO"})
result=product.find()
for product in result:
    print(product)

