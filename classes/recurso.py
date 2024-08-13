class Recurso:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor