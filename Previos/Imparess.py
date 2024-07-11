#Solicite un numero al usuario y determine si el numero es o no es primo
num=int(input("Digite el numero que desea consultar si es primo o no primo"))
num2=num/1
if num%2 <= 0:
    print("no primo")
elif num%3 <= 0:
    if num%5 <= 0:
        print("no primo")
    else:
        print("primo")
else:
    print("primo")





#cidesenadev@gmail.com


