with open('files/prueba1.txt','+r')as f:
    f.write('Los mejores programadores del sena de Soacha son de la ficha 2826996')
    f.seek(0)
    print(f.read())


# f=open('files/prueba1.txt','+r')
# contenido=f.read()
# print(contenido)
# f.close()




