from persona import *

per1 = Persona("jymi hendryx",123456789,0)
per2 = Persona('Carlos Vives',43434,2000000)


def datosPersona(person):
    return f'{person.getNombre()} {person.getDocumento()}'

def instanciarObjeto(nombre,documento):
    return Persona(nombre,documento,0)

print(datosPersona(per1))
print(datosPersona(per2))

retornado=instanciarObjeto('Julio Iglesias',565656)
print(type(retornado))
print(retornado.getNombre())

#FUNCION PARA CALCULAR BASE DE COTIZACION
def calcularBase(person):
    return person.getSalario()*0.40

print(f'Base de cotización= {calcularBase(per2)}')





# print(p1.getNombre())

# p1.setNombre("carlos vives")
# p1.nombre="Silvestre Perez"
# print(p1.getNombre())