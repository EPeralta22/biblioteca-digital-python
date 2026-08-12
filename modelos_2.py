### T.P. Final - Sistema de Gestión de Biblioteca Digital - 1° Fichero - Módulo de Clases ###

# 1. Libros

class Libros:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self._disponible:
            raise ValueError(f"El libro {self._titulo} ya se encuentra prestado.")
        self._disponible = False
        print(f"Libro '{self._titulo}' marcado como prestado.")

    def devolver(self):
        if self._disponible:
            raise ValueError(f"El libro {self._titulo} ya se encuentra disponible en la biblioteca.")
        self._disponible = True
        print(f"Libro '{self._titulo}' marcado como disponible.")


# 2. Usuarios

class Usuarios:
    def __init__(self, id_usuario, nombre):
        self._id_usuario = id_usuario
        self.nombre = nombre
        self._libros_prestados = []

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        self._nombre = valor

    @property
    def libros_prestados(self):
        return list(self._libros_prestados)

    def prestar_libro(self, libro):
        if len(self._libros_prestados) >= 3:
            raise ValueError(f"El usuario {self._nombre} ya ha alcanzado su límite de libros.")
        if libro in self._libros_prestados:
            raise ValueError(f"El usuario {self._nombre} ya posee ese libro.")
        libro.prestar()
        self._libros_prestados.append(libro)
        print(f"El usuario {self._nombre} retiró con éxito el libro '{libro.titulo}'.")

    def devolver_libro(self, libro):
        if libro not in self._libros_prestados:
            raise ValueError(f"El usuario {self._nombre} no tiene prestado el libro '{libro.titulo}'.")
        libro.devolver()
        self._libros_prestados.remove(libro)
        print(f"El usuario {self._nombre} devolvió con éxito el libro '{libro.titulo}'.")
