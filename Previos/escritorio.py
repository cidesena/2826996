#Llene una lista de n elementos entre 0 y 100. El tamaño tambien es aleatorio entre 5 y 20, buscar las posiciones pares y sumar los numeros, buscar las posiciones impares y sumar los numeros 

import random 
    
tamaño_lista=random.randint(5,20) 

print(f'El tamaño de la lista es: {tamaño_lista}' )

lista=[]
for n in range(0,tamaño_lista):
    numero=random.randint(0,100)
    lista.append(numero)

print(lista)

suma_par=0
for i in range(1,tamaño_lista,2):
    suma_par+=lista[i]
    
print(f'La suma de los numeros en posiciones pares es {suma_par}')

suma_impar=0
for i in range(0,tamaño_lista,2):
    suma_impar+=lista[i]
    
print(f'La suma de los numeros en posiciones impares es {suma_impar}')
