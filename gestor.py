class GestorLibros:
    def __init__(self):
        """Inicializa el gestor con una lista vacía de libros."""
        self.libros = []

    def agregar_libro(self, titulo, autor, anio):
        """Agrega un libro a la colección."""
        libro = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio
        }
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado correctamente.")

    def eliminar_libro(self, titulo):
        """Elimina un libro de la colección por su título."""
        for libro in self.libros:
            if libro["titulo"] == titulo:
                self.libros.remove(libro)
                print(f"Libro '{titulo}' eliminado correctamente.")
                return
        print(f"Libro '{titulo}' no encontrado.")

    def buscar_libro(self, titulo):
        """Busca un libro por su título."""
        for libro in self.libros:
            if libro["titulo"] == titulo:
                return libro
        return None

    def listar_libros(self):
        """Lista todos los libros en la colección."""
        if not self.libros:
            print("No hay libros en la colección.")
        else:
            print("Libros en la colección:")
            for libro in self.libros:
                print(f"- {libro['titulo']} (Autor: {libro['autor']}, Año: {libro['anio']})")


# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorLibros()
    gestor.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    gestor.agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    gestor.listar_libros()
    libro = gestor.buscar_libro("Cien años de soledad")
    if libro:
        print(f"Libro encontrado: {libro}")
    gestor.eliminar_libro("Don Quijote de la Mancha")
    gestor.listar_libros()