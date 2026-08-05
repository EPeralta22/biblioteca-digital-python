# Sistema de Gestión de Biblioteca Digital

Sistema en Python diseñado para administrar el catálogo de una biblioteca, el registro de usuarios y el control de préstamos de libros con reglas de negocio específicas.

## Reglas de negocio e implementación

- Control de estado: Seguimiento de disponibilidad de libros (Disponible / Prestado).
- Límite de préstamos: Restricción de un máximo de 3 libros activos por usuario.
- Manejo de excepciones: Captura de errores ante intentos de retirar libros ocupados o superar el límite permitido.
- Sincronización de objetos: Interacción directa entre la entidad Libro y la lista de préstamos del usuario.
- Persistencia: Generación del archivo prestamos_activos.txt mediante el recorrido estructurado de los usuarios y sus préstamos activos.

## Estructura del repositorio

- modelos_2.py: Definición de las clases Libros y Usuarios.
- main_2.py: Casos de prueba, manejo de excepciones y exportación del reporte.
- README.md: Documentación del proyecto.

## Requisitos y Ejecución

- Requiere Python 3.x

Para ejecutar el proyecto:

python main.py