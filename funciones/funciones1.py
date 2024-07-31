def analizarLista(lista):
    tipos=[]
    for dato in lista:
        if type(dato) not in tipos:
            tipos.append(type(dato))
    return tipos, len(tipos)

lista=['sena',{},123,[],'cide',4.5]
print(analizarLista(lista))
tipos,tam=analizarLista(lista)
print(tipos)
print(tam)