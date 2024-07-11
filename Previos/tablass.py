class Fila:
    def _init_(self, course_code, name, duration):
        self.course_code = course_code
        self.name = name
        self.duration = duration

    def _str_(self):
        return f"{self.course_code}\t{self.name}\t{self.duration}"

class Tabla:
    def _init_(self):
        self.filas = []

    def agregar_fila(self, fila):
        self.filas.append(fila)

    def mostrar_tabla(self):
        for fila in self.filas:
            print(fila)

def ingresar_datos():
    tabla = Tabla()
    while True:
        course_code = input("Ingrese el valor para la course_code: ")
        name = input("Ingrese el valor para la name: ")
        duration = input("Ingrese el valor para la duration: ")

        fila = Fila(course_code, name, duration)
        tabla.agregar_fila(fila)

        continuar = input("¿quiere otra fila? (s/n): ")
        if continuar.lower() != 's':
            break

    return tabla

def main():
    tabla = ingresar_datos()
    print("\nTabla resultante:")
    tabla.mostrar_tabla()


if __name__ == "__main__":
    main()