# Clase base Animal
class Animal:
    # def hacer_sonido(self):
    #     raise NotImplementedError("Debe implementar el método hacer_sonido")
        #raise ZeroDivisionError
        #return 1/0
    
    def hacer_sonido(self):
        print("Los animales no hablan")

# Clase Perro que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: Guau")

# Clase Gato que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: Miau")

class Cerdo(Animal):
    pass

# chicobestia=Animal()
# chicobestia.hacer_sonido()



michi=Gato()
firulais=Perro()
babe=Cerdo()

michi.hacer_sonido()
firulais.hacer_sonido()
babe.hacer_sonido()
