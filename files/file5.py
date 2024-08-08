from Aprendiz import *

tam=int(input('cuantos objetos'))
for i in range(tam):
    n=input('ingrese nombre')
    a=input('ingrese apellido')
    c=input('ingrese correo')
    d=int(input('ingrese documento'))
    ob=Aprendiz(n,a,c,d)

    with open('files/aprendices.txt','a')as f:
        f.write(ob.info())
        f.write('\n')