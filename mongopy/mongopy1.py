import pymongo
import json
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
#cat.insert_one({"nombre":"helados"})
#print(cat.insert_many([{"nombre":"cocktails"},{"nombre":"infusiones"}]))
# with open("mongopy/listado.json") as f:
#     data=json.load(f)

cat.insert_many(data)

for doc in cat.find():
    print("----",doc)
