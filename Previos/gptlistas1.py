import random

# Generar un tamaño aleatorio de la lista entre 5 y 20
n = random.randint(5, 20)

# Llenar la lista con n elementos aleatorios entre 0 y 100
lista = [random.randint(0, 100) for _ in range(n)]

# Calcular la suma de los números pares e impares
suma_pares = sum(x for x in lista if x % 2 == 0)
suma_impares = sum(x for x in lista if x % 2 != 0)

# Mostrar resultados
print("Lista generada:", lista)
print("Suma de los números pares:", suma_pares)
print("Suma de los números impares:", suma_impares)
