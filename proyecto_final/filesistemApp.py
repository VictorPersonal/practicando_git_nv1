import tkinter as tk
from tkinter import messagebox
from filesistem import FileSystem

import tkinter as tk
from tkinter import messagebox
from filesistem import FileSystem

class FileSystemApp(tk.Tk):
    """
    Representa la interfaz gráfica del sistema de archivos usando Tkinter. Permite interactuar con el sistema de archivos
    para crear, eliminar, cambiar directorios, listar el contenido y buscar nodos.

    Atributos:
        fs (FileSystem): Instancia del sistema de archivos para interactuar con los datos.
        canvas (tk.Canvas): Área gráfica donde se dibuja el árbol de directorios.
        controls_frame (tk.Frame): Contenedor para los controles de la interfaz (botones, entradas, etc.).
        input_entry (tk.Entry): Campo de texto para ingresar nombres de directorios o archivos.
        lblAdvertencia (tk.Label): Etiqueta con instrucciones sobre cómo agregar carpetas o archivos.
        create_button (tk.Button): Botón para crear un nuevo nodo (archivo o carpeta).
        delete_button (tk.Button): Botón para eliminar un nodo existente.
        change_button (tk.Button): Botón para cambiar al directorio especificado.
        list_button (tk.Button): Botón para listar el contenido del directorio actual.
        search_button (tk.Button): Botón para buscar un nodo en el sistema de archivos.

    Métodos:
        __init__(self, fs): Constructor que inicializa la interfaz y configura los componentes.
        create_node(self): Crea un nuevo nodo (archivo o carpeta) en el directorio actual.
        delete_node(self): Elimina un nodo (archivo o carpeta) del directorio actual.
        change_directory(self): Cambia el directorio actual a uno especificado.
        list_directory(self): Muestra el contenido del directorio actual en una nueva ventana.
        search(self): Abre una ventana para buscar un nodo en el sistema de archivos.
        draw_tree(self): Dibuja el árbol de directorios en el canvas, representando la jerarquía de nodos.
    """

    def __init__(self, fs):
        """
        Inicializa la ventana principal de la aplicación, configurando el sistema de archivos,
        la interfaz gráfica y los componentes.

        Args:
            fs (FileSystem): Instancia del sistema de archivos para interactuar con los datos.
        """
        super().__init__()
        self.fs = fs
        self.title("Sistema de Archivos")
        self.geometry("600x450")

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

        # Instrucciones de uso
        self.lblAdvertencia = tk.Label(self.controls_frame, text="Para agregar una carpeta --> Colocar el nombre seguido de '/'. Ej: Fotos/\nPara los archivos solo coloque el nombre")
        self.lblAdvertencia.grid(row=1, column=1, columnspan=3)

        # Botones de control
        self.create_button = tk.Button(self.controls_frame, text="Crear", command=self.create_node)
        self.create_button.grid(row=2, column=0, padx=5, pady=5)
        self.delete_button = tk.Button(self.controls_frame, text="Eliminar", command=self.delete_node)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)
        self.change_button = tk.Button(self.controls_frame, text="Cambiar Directorio", command=self.change_directory)
        self.change_button.grid(row=2, column=2, padx=5, pady=5)
        self.list_button = tk.Button(self.controls_frame, text="Listar", command=self.list_directory)
        self.list_button.grid(row=2, column=3, padx=5, pady=5)
        self.search_button = tk.Button(self.controls_frame, text="Buscar", command=self.search)
        self.search_button.grid(row=2, column=4, padx=5, pady=5)

        # Dibujar el árbol inicial
        self.draw_tree()

    def create_node(self):
        """
        Crea un nuevo nodo (archivo o carpeta) en el directorio actual. Si se ingresa un nombre con '/', 
        se interpreta como carpeta. Si no, se interpreta como archivo. Si la operación es exitosa, 
        se actualiza la interfaz con un mensaje de éxito.
        """
        self.lblAdvertencia.destroy()
        name = self.input_entry.get()
        tipo = "carpeta" if name.endswith("/") else "archivo"
        
        try:
            nodo_agregado = self.fs.crear(name, tipo)
            if nodo_agregado:
                self.draw_tree()
                tk.messagebox.showinfo("Info", "Agregado :)")  # Solo mostrar si fue agregado
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def delete_node(self):
        """
        Elimina un nodo (archivo o carpeta) del directorio actual. Si la eliminación es exitosa, 
        se actualiza la interfaz con un mensaje de éxito. Si el nodo no se encuentra, se muestra un mensaje de error.
        """
        name = self.input_entry.get()
        try:
            self.fs.eliminar(name)
            self.draw_tree()
            tk.messagebox.showinfo("Éxito", f"'{name}' eliminado correctamente.")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def change_directory(self):
        """
        Cambia el directorio actual a uno especificado por el usuario. Si el cambio es exitoso, 
        se muestra un mensaje con la ubicación actual del directorio. Si no se puede cambiar (por ejemplo, 
        si el directorio no existe), se muestra un mensaje de error.
        """
        name = self.input_entry.get()
        try:
            self.fs.cambiar_directorio(name)
            self.draw_tree()
            tk.messagebox.showinfo("Excelente", f"El directorio donde está ubicado es: '{self.fs.directorio_actual.nombre}'")
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def list_directory(self):
        """
        Muestra el contenido del directorio actual en una nueva ventana. Si ocurre un error al obtener el contenido, 
        se muestra un mensaje de error.
        """
        try:
            resultados = self.fs.listar()
            ventana_mostrar_resultados = tk.Toplevel(self)
            ventana_mostrar_resultados.title("Aquí verás la informacion que contiene el directorio actual")
            ventana_mostrar_resultados.geometry("400x300")
            texto = tk.Text(ventana_mostrar_resultados)
            texto.grid(row=0, column=0)
            texto.insert(tk.END, resultados + "\n")
            texto.config(state="disabled")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def search(self):
        """
        Abre una nueva ventana para permitir la búsqueda de un nodo en el sistema de archivos. 
        Muestra los resultados de la búsqueda en un área de texto.
        """
        ventana_buscar = tk.Toplevel(self)
        ventana_buscar.title("Buscar nodo")
        ventana_buscar.geometry("400x200")
        lblBuscar = tk.Label(ventana_buscar, text="Ingrese el nodo a buscar: ")
        lblBuscar.grid(row=0, column=0)
        txtBuscar = tk.Entry(ventana_buscar)
        txtBuscar.grid(row=0, column=1)
        area_resultado_esperado = tk.Text(ventana_buscar, state="disabled", width=25, height=25)
        area_resultado_esperado.grid(row=1, column=1, pady=10)

        def buscar_nodo():
            nombre = txtBuscar.get()
            if not nombre.strip():
                tk.messagebox.showwarning("Advertencia", "Debe ingresar un nombre para buscar")
                return
            resultado = self.fs.buscar(nombre)
            area_resultado_esperado.config(state="normal")
            area_resultado_esperado.delete(1.0, tk.END)
            if resultado:
                area_resultado_esperado.insert(tk.END, f"Se encontró el nodo:\n{str(resultado)}")
            else:
                area_resultado_esperado.insert(tk.END, "No se encontró ningun nodo con ese nombre")
            area_resultado_esperado.config(state="disabled")

        btnBuscar = tk.Button(ventana_buscar, text="Buscar", command=buscar_nodo)
        btnBuscar.grid(row=0, column=2, padx=5, pady=5)

    def draw_tree(self):
        """
        Dibuja el árbol de directorios en el canvas. Los nodos y sus hijos se dibujan recursivamente.
        """
        self.canvas.delete("all")

        def draw_node(nodo, x, y, depth=0):
            """
            Dibuja un nodo del sistema de archivos en el canvas, representando su nombre y conectando 
            recursivamente a sus hijos con líneas.

            Args:
                nodo (Nodo): El nodo que se va a dibujar (archivo o carpeta).
                x (int): La coordenada X donde se debe dibujar el nodo en el canvas.
                y (int): La coordenada Y donde se debe dibujar el nodo en el canvas.
                depth (int, opcional): El nivel de profundidad del nodo en el árbol. Se usa para calcular
                                    la distancia entre los nodos en el canvas. Por defecto es 0.

            Este método realiza lo siguiente:
                1. Dibuja un rectángulo para representar al nodo.
                2. Dibuja el nombre del nodo dentro del rectángulo.
                3. Si el nodo tiene hijos, dibuja líneas conectando al nodo con sus hijos, y
                llama recursivamente para dibujar los hijos de manera jerárquica.
            """
            # Dibujar el rectángulo para representar al nodo
            rect = self.canvas.create_rectangle(x, y, x + 100, y + 30, fill="lightblue")
            
            # Dibujar el nombre del nodo dentro del rectángulo
            text = self.canvas.create_text(x + 50, y + 15, text=nodo.nombre)

            # Si el nodo tiene hijos, dibujarlos
            if nodo.hijos:
                new_x = x - 150 * len(nodo.hijos) // 2  # Calcula la posición X de los hijos para centrar los nodos
                for i, hijo in enumerate(nodo.hijos):
                    # Calcula las posiciones X y Y de cada hijo
                    child_x = new_x + i * 150
                    child_y = y + 70  # Distancia en el eje Y entre padres e hijos

                    # Dibujar una línea de conexión entre el nodo actual y el hijo
                    self.canvas.create_line(x + 50, y + 30, child_x + 50, child_y)

                    # Llamada recursiva para dibujar el hijo
                    draw_node(hijo, child_x, child_y, depth + 1)

        # Llamada inicial para dibujar el árbol desde la raíz
        draw_node(self.fs.raiz, 300, 20)

# Ejemplo de uso
if __name__ == "__main__":
    fs = FileSystem()
    app = FileSystemApp(fs)
    app.mainloop()
