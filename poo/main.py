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

def incremento(person, p):
    s=person.getSalario()
    s+=(s*p)
    person.setSalario(s)
    return person
print('-'*30)
incremento(per2,0.10)
print(per2.getSalario())





# print(p1.getNombre())

# p1.setNombre("carlos vives")
# p1.nombre="Silvestre Perez"
# print(p1.getNombre())