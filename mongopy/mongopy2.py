import pymongo
import pprint
from Producto import *
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
# for doc in myorden.find():
#     pprint.pp(doc["mesero"])
#     pprint.pp(doc["detalleOrden"])
    
for detalle in myorden.find():    
    pprint.pp(detalle["mesero"])
    #pprint.pp(detalle['detalleOrden'][0])
    for elemento in detalle['detalleOrden']:
        #pprint.pp(elemento['nombre'])
        #pprint.pp(elemento['nombre'])
        vcantidad=elemento['cantidad']
        vnombre=elemento['nombre']
        vprecio=elemento['precio']
        vcategoria=elemento['categoria']
        vsubtotal=elemento['subtotal']        
        ob=Producto(vcantidad,vnombre,vprecio,vcategoria,vsubtotal)

print(ob)




