from classes.usuario import Usuario
from classes.bibliotecario import Bibliotecario
from classes.libro import Libro
from classes.revista import Revista

class Pedido:
    def __init__(self, codigoPedido, fecha, usuario, bibliotecario):
        self.__codigoPedido = codigoPedido
        self.__fecha = fecha
        self.__usuario = usuario
        self.__bibliotecario = bibliotecario
        self.__libros = []
        self.__revistas = []

    def get_codigoPedido(self):
        return self.__codigoPedido

    def set_codigoPedido(self, codigoPedido):
        self.__codigoPedido = codigoPedido

    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha

    def getUsuario(self):
        return self.__usuario

    def setUsuario(self, usuario):
        #self.__usuario = usuario
        self.__usuario=Usuario()

    def getBibliotecario(self):
        return self.__bibliotecario

    def setBibliotecario(self, bibliotecario):
        self.__bibliotecario = bibliotecario

    def getLibros(self):
        return self.__libros

    def getRevistas(self):
        return self.__revistas

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def agregarRevista(self, revista):
        self.__revistas.append(revista)
