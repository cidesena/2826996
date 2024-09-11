import pprint
import pymongo
from Producto import *
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
#print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
Mesero=basedatos["Mesero"]
datos=myorden.find({},{"mesero":1,"_id":0})
for m in datos:
    #pprint.pp(m)
    print(Mesero.insert_one(m))


