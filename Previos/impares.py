#socilite un numero al usuario y determine si el numero es primo o no es primo

def primo():
    numero=int(input('Ingrese un numero para verificar si es primo o no: '))
    if numero <= 1:
        print(f'{numero} no es un numero primo.')

primo()
