from Aprendiz import *
from Curso import *
ap1=Aprendiz('Juan Salazar',12345,2826996)
c1=Curso('python1',1)
ap1.agregarCurso(c1)
#print(ap1.getCursos())
for c in ap1.getCursos():
    print(c.getNomCurso())
ap1.agregarProgBienestar('Danzas','cultural')
ap1.agregarProgBienestar('Apoyo de Sostenimiento','social')

for p in ap1.getProgBienestar():
    print(p.getNomProgBienestar())

del(ap1)

print(c1)


