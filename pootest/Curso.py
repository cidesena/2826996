class Curso():
    def __init__(self,nomCurso,codigo):
        self.__nomCurso=nomCurso
        self.__codigo=codigo
    
    def getNomCurso(self):
        return self.__nomCurso