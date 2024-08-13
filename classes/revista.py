from classes.recurso import Recurso

class Revista(Recurso):
    def __init__(self, titulo, autor, codigoRevista):
        super().__init__(titulo, autor)
        self.__codigoRevista = codigoRevista

    def get_codigoRevista(self):
        return self.__codigoRevista

    def set_codigoRevista(self, codigoRevista):
        self.__codigoRevista = codigoRevista