class Libro:
    def __init__(self, titulo, autor, paginas):
        # Inicializamos los atributos de la clase
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    
    def __str__(self):
        return f"{self.titulo} por {self.autor}"


    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"



libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)


print(str(libro1))
print(repr(libro1))

print(str(libro2))
print(repr(libro2))
