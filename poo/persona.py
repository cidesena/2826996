class Persona ():
    def __init__(self,nombre,documento,salario):
        self.__nombre = nombre
        self.__documento = documento
        self.__salario = salario
        
    def getNombre (self):
        return self.__nombre
    
    def setNombre (self,nombre):
        self.__nombre = nombre
    
    def getDocumento (self):
        return self.__documento
    
    def setDocumento (self,documento):
        self.__documento = documento
    
    def getSalario (self):
        return self.__salario
    
    def setSalario (self,salario):
        self.__salario = salario