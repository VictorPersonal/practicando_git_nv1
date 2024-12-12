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
        self.search_button=tk.Button(self.controls_frame, text="Buscar", command=self.search)
        self.search_button.grid(row=1, column=4, padx=5, pady=5)
        

        # Dibujar el árbol inicial
        self.draw_tree()

    def create_node(self):
        name = self.input_entry.get()
        
        if (name.endswith("/")):
            tipo="carpeta"
        else:
            tipo="archivo"
        
        try:
            # Intentar agregar el nodo
            nodo_agregado = self.fs.crear(name, tipo)  # Ahora retorna si el nodo fue agregado
            if nodo_agregado:
                self.draw_tree()
                tk.messagebox.showinfo("Info", "Agregado :)")  # Solo mostrar si fue agregado
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def delete_node(self):
        name = self.input_entry.get()  # Obtener el nombre del nodo a eliminar
        try:
            # Intentar eliminar el nodo
            self.fs.eliminar(name)  
            self.draw_tree()  # Redibuja el árbol si se elimina correctamente
            tk.messagebox.showinfo("Éxito", f"'{name}' eliminado correctamente.")
            
        except ValueError as e:
            # Captura cualquier ValueError (incluyendo el que hemos lanzado en caso de no encontrar el nodo)
            tk.messagebox.showerror("Error", str(e))
        

        self.draw_tree()

    def change_directory(self):
        name = self.input_entry.get()
        try:
            self.fs.cambiar_directorio(name)
            self.draw_tree()
            tk.messagebox.showinfo("Excelente",f"El directorio donde está ubicado es: '{self.fs.directorio_actual.nombre}'")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def list_directory(self):
        try:

            resultados = self.fs.listar()

            ventana_mostrar_resultados=tk.Toplevel(self)
            ventana_mostrar_resultados.title("Aquí verás la informacion que contiene el directorio actual")
            ventana_mostrar_resultados.geometry("400x300")
            texto=tk.Text(ventana_mostrar_resultados)
            texto.grid(row=0, column=0)

            texto.insert(tk.END, resultados + "\n")

            texto.config(state="disabled")


        except Exception as e:
            tk.messagebox.showerror("Error", str(e))


    def search(self):
        ventana_buscar=tk.Toplevel(self)
        ventana_buscar.title("Buscar nodo")
        ventana_buscar.geometry("400x200")
        lblBuscar=tk.Label(ventana_buscar,text="Ingrese el nodo a buscar: ")
        lblBuscar.grid(row=0, column=0)
        txtBuscar=tk.Entry(ventana_buscar)
        txtBuscar.grid(row=0, column=1)
        area_resultado_esperado= tk.Text(ventana_buscar,state="disabled")
        area_resultado_esperado.grid(row=1,column=1)
        
        
        def buscar_nodo():
            nombre=txtBuscar.get()
            if not nombre.strip():
                tk.messagebox.showwarring("Advertencia","Debe ingresar un nombre para buscar")
                return
            resultado=fs.buscar(nombre)
            area_resultado_esperado.config(state="normal")
            area_resultado_esperado.delete(1.0,tk.END)
            if resultado:
                area_resultado_esperado.insert(tk.END, f"Se encontró el nodo:\n{str(resultado)}")
            else:
                area_resultado_esperado.insert(tk.END,"No se encontró ningun nodo con ese nombre")
            area_resultado_esperado.config(state="disabled")
        btnBuscar=tk.Button(ventana_buscar, text="Buscar", command=buscar_nodo)
        btnBuscar.grid(row=2,column=0)

        



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
