from persona import *

per1 = Persona("jymi hendryx",123456789)
per2 = Persona('Carlos Vives',43434)

def datosPersona(person):
    return f'{person.getNombre()} {person.getDocumento()}'

def instanciarObjeto(nombre,documento):
    return Persona(nombre,documento)

print(datosPersona(per1))
print(datosPersona(per2))

retornado=instanciarObjeto('Julio Iglesias',565656)
print(type(retornado))
print(retornado.getNombre())






# print(p1.getNombre())

# p1.setNombre("carlos vives")
# p1.nombre="Silvestre Perez"
# print(p1.getNombre())