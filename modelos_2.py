### T.P. Final - Sistema de Gestión de Biblioteca Digital - 1° Fichero - Módulo de Clases ###

# 1. Libros

class Libros:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    def prestar(self):
        if not self.disponible:
            raise ValueError(f"El libro {self.titulo} ya se encuentra prestado.")
        self.disponible = False
        print(f"Libro '{self.titulo}' marcado como prestado.")
    def devolver(self):
            if self.disponible:
                raise ValueError(f"El libro {self.titulo} ya se encuentra disponible en la biblioteca.")
            self.disponible = True
            print(f"Libro '{self.titulo}' marcado como disponible.")
        

# 2. Usuarios

class Usuarios:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []
    def prestar_libro(self, libro):
        if len(self.libros_prestados) >= 3:
            raise ValueError(f"El usuario {self.nombre} ya ha alcanzado su límite de libros.")
        if libro in self.libros_prestados:
            raise ValueError(f"El usuario {self.nombre} ya posee ese libro.")
        libro.prestar()
        self.libros_prestados.append(libro)
        print(f"El usuario {self.nombre} retiró con éxito el libro '{libro.titulo}'.")
    def devolver_libro(self, libro):
        if libro not in self.libros_prestados:
            raise ValueError(f"El usuario {self.nombre} no tiene prestado el libro '{libro.titulo}'.")
        libro.devolver()
        self.libros_prestados.remove(libro)
        print(f"El usuario {self.nombre} devolvió con éxito el libro '{libro.titulo}'.")