def cantidadLineas(archivo):
    with open(archivo,'r')as f:
        tam=f.readlines()
        return len(tam) 

print(cantidadLineas('files/prueba2.txt'))