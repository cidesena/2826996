import pprint
import pymongo
from Producto import *
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
#print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
consulta=myorden.find({},{"detalleOrden.subtotal":1,"_id":1})
for doc in consulta:
    pprint.pp(doc["_id"])
    sum=0
    for objeto in doc["detalleOrden"]:
        #pprint.pp(objeto)
        #pprint.pp(objeto["subtotal"])
        sum=sum+objeto["subtotal"]
    print("Total =",sum)
