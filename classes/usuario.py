from persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, regional, doc, telefono, mail):
        super().__init__(nombre, regional)
        self.__doc = doc
        self.__telefono = telefono
        self.__mail = mail

    def getDoc(self):
        return self.__doc

    def setDoc(self, doc):
        self.__doc = doc
    
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__telefono = telefono
        
    def getMail(self):
        return self.__mail
        
    def setMail(self, mail):
        self.__mail = mail