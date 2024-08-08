cont=0
flag=True
while flag: 
    nombre=input('Escriba nombre')
    doc=int(input('ingrse documento'))
    c=f'{nombre} {doc}\n'
    with open('files/prueba2.txt','a')as f:
        f.write(c)
    cont+=1
    if cont>=3:
        flag=False
