from classes.recurso import Recurso

class Libro(Recurso):
    def __init__(self, titulo, autor, codigoLibro):
        super().__init__(titulo, autor)
        self.__codigoLibro = codigoLibro

    def get_codigoLibro(self):
        return self.__codigoLibro

    def set_codigoLibro(self, codigoLibro):
        self.__codigoLibro = codigoLibro