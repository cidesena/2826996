import pymongo
cliente=pymongo.MongoClient("mongodb://localhost:27017/")
print(cliente.list_database_names())
basedatos=cliente["resbarSalvador"]
cat=basedatos["Categoria"]
myorden=basedatos["Orden"]
#print(type(cat))
data=myorden.find({'detalleOrden.cantidad':{'$gt':3}},{'nombre':1,'mesero':1})
#print(cat.find())
for doc in data:
    print(doc)
