### T.P. Final - Sistema de Gestión de Biblioteca Digital - 1° Fichero - Módulo de Clases ###

# 1. Importación Modular

from modelos_2 import Libros, Usuarios

# 2. Función de Persistencia

def guardar_reporte(lista_usuarios, nombre_archivo="prestamos_activos.txt"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("=== REPORTE DE PRÉSTAMOS ACTIVOS ===\n\n")
               
        # 1. Primer for: Recorremos cada usuario de la lista
        for usuario in lista_usuarios:
            archivo.write(f"Usuario: {usuario.nombre} (ID: {usuario.id_usuario})\n")
            archivo.write("Libros retirados:\n")
            
        # 2. Verificar si el usuario tiene libros prestados
            if not usuario.libros_prestados:
                archivo.write("  - Sin libros prestados actualmente.\n")
            else:
                # 3. Segundo for: Recorremos los libros del usuario actual
                for libro in usuario.libros_prestados:
                    archivo.write(f"  - Título: '{libro.titulo}' | Autor: {libro.autor} | ISBN: {libro.isbn}\n")
            
            archivo.write("\n" + "-"*40 + "\n\n") # Un separador prolijo entre usuarios
            
    print(f"📄 Reporte guardado con éxito en '{nombre_archivo}'.")

# 3. Bloque de Ejecución Principal (Pruebas Integrales)

u1 = Usuarios(1001, "Lucas")
u2 = Usuarios(1002, "Sofía")

l1 = Libros("La Caída de los Cuchillas", "Alexander Magno", 145236)
l2 = Libros("Estrella del Alba", "Christopher Smith", 478569)
l3 = Libros("Los mil y un pucheros", "Ronald McBurguer", 122896)
l4 = Libros("Folklore y Cultura", "Fito García", 986235)

print("--- SOLICITUD DE PRESTAMO ---")

u1.prestar_libro(l1)
u1.prestar_libro(l4)

try:
    u2.prestar_libro(l1)
except ValueError as e:
    print(f"Error de prestamo capturado: {e}")

try:
    u1.prestar_libro(l2)
    u1.prestar_libro(l3)
except ValueError as e:
    print(f"Error de prestamo capturado: {e}")

print("--- INGRESANDO DEVOLUCIONES ---")

u1.devolver_libro(l1)

print("\n--- GENERACIÓN DE REPORTE ---")

lista_usuarios = [u1, u2]
guardar_reporte(lista_usuarios)