from abc import ABC, abstractmethod



class Publicacion(ABC):
    @abstractmethod
    def informacion(self):

        pass

    @abstractmethod
    def resumen(self):

        pass



class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacion(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"

    def resumen(self):
        return f"Un libro fascinante titulado '{self.titulo}' escrito por {self.autor}."



class Revista(Publicacion):
    def __init__(self, nombre, numero, fecha):
        self.nombre = nombre
        self.numero = numero
        self.fecha = fecha

    def informacion(self):
        return f"Nombre: {self.nombre}\nNúmero: {self.numero}\nFecha: {self.fecha}"

    def resumen(self):
        return f"Revista '{self.nombre}' número {self.numero} publicada en {self.fecha}."



libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
revista1 = Revista("National Geographic", 305, "Octubre 2023")


print("Información del Libro:")
print(libro1.informacion())
print(libro1.resumen())

print("\nInformación de la Revista:")
print(revista1.informacion())
print(revista1.resumen())
