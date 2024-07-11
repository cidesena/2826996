import random

n = random.randint(5, 10)
lista = [random.randint(0, 100) for l in range(n)]
# sumaPares = sum(numero for numero in lista if numero % 2 == 0)
# sumaImpares = sum(numero for numero in lista if numero % 2!= 0)
print(lista)
sum=0
for numero in lista:
    #print(numero)
    if numero%2==0:
        sum+=numero 
    #(acumulador)sum=sum+numero
    #(contador)var=var+constante ; i=i+1; i+=1
print(sum)