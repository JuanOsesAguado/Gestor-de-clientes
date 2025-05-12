import tkinter as tk
from tkinter import messagebox
from gestor import GestorLibros

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Biblioteca")
        self.gestor = GestorLibros()

        # Etiquetas y campos de entrada
        tk.Label(root, text="Título:").grid(row=0, column=0, padx=5, pady=5)
        self.titulo_entry = tk.Entry(root)
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
        self.autor_entry = tk.Entry(root)
        self.autor_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Año:").grid(row=2, column=0, padx=5, pady=5)
        self.anio_entry = tk.Entry(root)
        self.anio_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        tk.Button(root, text="Agregar Libro", command=self.agregar_libro).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(root, text="Eliminar Libro", command=self.eliminar_libro).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(root, text="Listar Libros", command=self.listar_libros).grid(row=4, column=0, columnspan=2, pady=5)

        # Área de texto para mostrar la lista de libros
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        anio = self.anio_entry.get()

        if titulo and autor and anio.isdigit():
            self.gestor.agregar_libro(titulo, autor, int(anio))
            messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos correctamente.")

    def eliminar_libro(self):
        titulo = self.titulo_entry.get()

        if titulo:
            self.gestor.eliminar_libro(titulo)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, ingresa el título del libro a eliminar.")

    def listar_libros(self):
        self.text_area.delete(1.0, tk.END)
        if not self.gestor.libros:
            self.text_area.insert(tk.END, "No hay libros en la colección.\n")
        else:
            for libro in self.gestor.libros:
                self.text_area.insert(tk.END, f"- {libro['titulo']} (Autor: {libro['autor']}, Año: {libro['anio']})\n")

    def limpiar_campos(self):
        self.titulo_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.anio_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()