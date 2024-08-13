from classes.persona import Persona

class Bibliotecario(Persona):
    def __init__(self, nombre, regional, id):
        super().__init__(nombre, regional)
        self.__id = id

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id