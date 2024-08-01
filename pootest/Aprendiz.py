from Persona import *
from Curso import *
from Bienestar import *

class Aprendiz(Persona):
    def __init__(self, nombre, documento,ficha):
        super().__init__(nombre, documento)
        self.__ficha=ficha
        self.__cursos=[]
        self.__progBienestar=[]
    
    def agregarCurso(self,nuevoCurso):
        self.__cursos.append(nuevoCurso)
    
    def agregarProgBienestar(self,nomPrograma,tipo):
        programa=Bienestar(nomPrograma,tipo)
        self.__progBienestar.append(programa)

    def getCursos(self):
        return self.__cursos

    def getProgBienestar(self):
        return self.__progBienestar