import tkinter as tk
from tkinter import ttk
import sqlite3


class ventanaHistorial(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Historial")
        self.geometry("500x300")
        
        self.crear_widgets()
        self.cargar_datos()

    def crear_widgets(self):
        self.pestanas = ttk.Notebook(self)
        self.pestanas.pack(fill="both", expand=True)

        # Pestaña "Historial"
        self.tab_historial = ttk.Frame(self.pestanas)
        self.pestanas.add(self.tab_historial, text="Historial")

        self.tabla = ttk.Treeview(self.tab_historial,
                                  columns=("nombre", "extension"),
                                  show="headings")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("extension", text="Extensión")
        self.tabla.pack(fill="both", expand=True)

        self.etiqueta = ttk.Label(self.tab_historial, text="Selecciona un archivo")
        self.etiqueta.pack(pady=5)

        # Evento: se ejecuta al seleccionar una fila
        #self.tabla.bind("<<TreeviewSelect>>", self.al_seleccionar)

    def cargar_datos(self):
        self.tabla.delete(*self.tabla.get_children())  # vaciar la tabla
        for id_, nombre, ext in self.conn.execute("SELECT id, nombre, extension FROM archivos"):
            self.tabla.insert("", "end", iid=str(id_), values=(nombre, ext))

    def al_seleccionar(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            self.etiqueta.config(text=f"id en la BD: {seleccion[0]}")


