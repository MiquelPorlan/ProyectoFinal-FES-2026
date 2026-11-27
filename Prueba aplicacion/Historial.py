import tkinter as tk
from tkinter import ttk

class ventanaHistorial(tk.Toplevel):
    def __init__(self, master, ruta):
        super().__init__(master)
        
        self.title("Historial")
        self.transient(master)
        
        ## Mostrar tabla       
        self.marco = ttk.Treeview(self, 
                                  columns=("nom","ruta"),
                                  show="headings")
        self.marco.heading("nom", text = "nombre")
        self.marco.heading("ruta", text = "destino")
        self.marco.column("nom", width=100, minwidth=100, stretch=True, anchor="w")
        self.marco.column("ruta", width=300, minwidth=300, stretch=True, anchor="w")
        self.marco.pack(fill="both", expand=True)
        
        self.marco.insert("", "end", values=("nombreEjemplo1", "rutaEjemplo"))

        
