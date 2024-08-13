class Persona:
    def __init__(self, nombre, regional):
        self.__nombre = nombre
        self.__regional = regional

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getRegional(self):
        return self.__regional

    def setRegional(self, regional):
        self.__regional = regional