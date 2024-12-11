import tkinter as tk
from tkinter import messagebox
from filesistem import FileSystem

class FileSystemApp(tk.Tk):
    def __init__(self, fs):
        super().__init__()
        self.fs = fs
        self.title("Sistema de Archivos")
        self.geometry("600x400")

        # Canvas para mostrar el árbol
        self.canvas = tk.Canvas(self, bg="white", width=600, height=300)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Frame de controles
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar columnas para que se expandan
        for i in range(4):
            self.controls_frame.grid_columnconfigure(i, weight=1)

        # Entrada de texto
        self.input_label = tk.Label(self.controls_frame, text="Nombre o Ruta:")
        self.input_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.input_entry = tk.Entry(self.controls_frame)
        self.input_entry.grid(row=0, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

        # Botones de control
        self.create_button = tk.Button(self.controls_frame, text="Crear", command=self.create_node)
        self.create_button.grid(row=1, column=0, padx=5, pady=5)
        self.delete_button = tk.Button(self.controls_frame, text="Eliminar", command=self.delete_node)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)
        self.change_button = tk.Button(self.controls_frame, text="Cambiar Directorio", command=self.change_directory)
        self.change_button.grid(row=1, column=2, padx=5, pady=5)
        self.list_button = tk.Button(self.controls_frame, text="Listar", command=self.list_directory)
        self.list_button.grid(row=1, column=3, padx=5, pady=5)

        # Dibujar el árbol inicial
        self.draw_tree()

    def create_node(self):
        name = self.input_entry.get()
        
        if (name.endswith("/")):
            tipo="carpeta"
        else:
            tipo="archivo"
        try:
            self.fs.crear(name, tipo)
            self.draw_tree()
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def delete_node(self):
        name = self.input_entry.get()  # Obtener el nombre del nodo a eliminar
        try:
            # Intentar eliminar el nodo
            if self.fs.eliminar(name):  # Verifica si la eliminación fue exitosa
                self.draw_tree()  # Redibuja el árbol si se elimina correctamente
                tk.messagebox.showinfo("Éxito", f"'{name}' eliminado correctamente.")
            else:
                # Si no se pudo eliminar, mostrar un mensaje de error
                raise ValueError(f"'{name}' no encontrado para eliminar.")  # Lanza un ValueError para manejar el error
        except ValueError as e:
            # Captura cualquier ValueError (incluyendo el que hemos lanzado en caso de no encontrar el nodo)
            tk.messagebox.showerror("Error", str(e))
        

        self.draw_tree()

    def change_directory(self):
        name = self.input_entry.get()
        try:
            self.fs.cambiar_directorio(name)
            self.draw_tree()
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def list_directory(self):
        try:
            resultados = self.fs.listar()
            self.output_text = '\n'.join(resultados)
            self.canvas.delete("all")  # Limpiar el canvas antes de mostrar el nuevo texto
            self.canvas.create_text(10, 10, text=self.output_text, anchor="nw", font=("Arial", 10))
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))


    def draw_tree(self):
        # Limpiar Canvas
        self.canvas.delete("all")
        
        # Dibujar el árbol recursivamente
        def draw_node(nodo, x, y, depth=0):
            # Dibujar el nodo actual
            rect = self.canvas.create_rectangle(x, y, x + 100, y + 30, fill="lightblue")
            text = self.canvas.create_text(x + 50, y + 15, text=nodo.nombre)

            # Dibujar hijos
            if nodo.hijos:
                new_x = x - 150 * len(nodo.hijos) // 2
                for i, hijo in enumerate(nodo.hijos):
                    child_x = new_x + i * 150
                    child_y = y + 70
                    self.canvas.create_line(x + 50, y + 30, child_x + 50, child_y)  # Línea hacia el hijo
                    draw_node(hijo, child_x, child_y, depth + 1)

        # Llamada inicial para el nodo raíz
        draw_node(self.fs.raiz, 300, 20)


# Ejemplo de uso
if __name__ == "__main__":
    fs = FileSystem()
    app = FileSystemApp(fs)
    app.mainloop()
