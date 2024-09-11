import pprint
import pymongo
from Producto import *
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
#print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
Mesero=basedatos["Mesero"]
# for m in Mesero.find():
#     q={"_id":m["_id"]}
#     nuevo={"$set":{"restaurante":"Gran Plaza"}}
#     Mesero.update_one(q,nuevo)

for m in Mesero.find():
    pprint.pp(m)
