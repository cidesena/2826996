class Aprendiz:
    def __init__(self,nombre,apellido,correo,doc):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        self.__doc=doc
    def info(self):
        return f"{self.__nombre} {self.__apellido} {self.__correo} {self.__doc}"
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCorreo(self):
        return self.__correo
    
    def getDocumento(self):
        return self.__doc