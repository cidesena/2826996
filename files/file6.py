from Aprendiz import *
with open('files/aprendices.txt','r') as f:
    data=f.readlines()

listado=[]
for linea in data:
    apr=linea.split()
    n=apr[0]
    a=apr[1]
    c=apr[2]
    d=apr[3]
    ob=Aprendiz(n,a,c,d)
    listado.append(ob)

for aprendiz in listado:
    print(aprendiz.getNombre())

