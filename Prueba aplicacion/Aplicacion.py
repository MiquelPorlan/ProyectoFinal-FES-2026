## insertar librerias necesarias ## 
import threading 
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


class App(tk.Tk):## creacion de la clase App con tk.Tk como clase padre, de la que hereda las funciones
    def __init__(self): ## Setup de la ventana de la App
        super().__init__() ## super. hace referencia a la clase padre, __init__ ejecuta el Setup de esa clase padre
        
        ## self. hace referncia a varibles del propio objeto, se mantienen una vez acabada la funcion como varibles del objeto
        
        self.title("Compresor de archivos") ## estas tres son varibles de la clase padre, creadas en super().__init__()
        self.geometry("500x170")
        self.resizable(False, False)
        
        self.ruta1 = tk.StringVar()## Estas tres variables las creamos nosotros par poder usarlas en las funciones que hara la app
        self.ruta2 = tk.StringVar()
        self.modo = tk.StringVar(value="comprimir") ## Stringvar son variables de tkinter para usarlas en widgets esto les asigna un valor inicial y el tipo de la varible
        self.estado = tk.StringVar(value="Selecciona un archivo para empezar.") ## son el equivalente a (numero = int(12))
        
        marco = ttk.Frame(self, padding=15) ## crea un contenedor al que llama marco, padding es una especie de sangrado
        marco.pack(fill="both", expand=True) ## adapta automaticamente el tamaño del marco para que ocupe todo el espacio que puede
        
        ttk.Label(marco, text="Archivo entrada:").grid(row=0, column=0, sticky="w") ## marco es el padre que acabamos de crear
        ttk.Entry(marco, textvariable=self.ruta1, width=45).grid(row=0, column=1, sticky="we", pady=4)
        ## grid divide la ventana en cachos y ordena los diferentes frames en funcion de la posicion, pady deja un espacio arriba, viene de "pad" y el eje "y"
        ## el argumento sticky indica a que borde se debe de pegar, w=izquierda | we=rellenar de izierda a derecha
        
        ttk.Button(marco, text="Examinar…", command=lambda: self.encontrarRuta(self.ruta1)).grid(row=0, column=2, padx=(8, 0))
        
        
        opciones = ttk.Frame(marco)
        opciones.grid(row=2, column=0, columnspan=2, sticky="w", pady=8) ## crea una malla para el marco de opciones, le da hasta el espaci de dos columnas
        ttk.Radiobutton(opciones, text="Comprimir", variable=self.modo, value="Comprimir").pack(side="left", padx=(0,20))
        ttk.Radiobutton(opciones, text="Descomprimir", variable=self.modo, value="Descomprimir").pack(side="left")
        ## crea dos botones circulares, con el nombre de la funcion que toma y le asigna un valor, al usar ambos el mismo valor, al pulsar uno el otro se desactiva.
        ## pack coloca uno al lado del otro en vez de apilados, al no poder mezclar, grid y pack se crea un frame con grid sobre el que se usara pack  
        
        ttk.Label(marco, text="Archivo salida:").grid(row=3, column=0, sticky="w") 
        ttk.Entry(marco, textvariable=self.ruta2, width=45).grid(row=3, column=1, sticky="we", pady=4)
        ttk.Button(marco, text="Examinar…", command=lambda: self.encontrarRuta(self.ruta2)).grid(row=3, column=2, padx=(8, 0))
        
        ttk.Button(marco, text="Ejecutar", command= self.ejecutarPrograma).grid(row=4, column=0, columnspan= 3, sticky="we")
    
    def encontrarRuta(self, archivo):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo")
        if ruta: ## verificar que no se guarde nada si se cierra la ventana emergente sin seleccionar opcion
            archivo.set(ruta)
    
    def ejecutarPrograma(self): 
        a = self.ruta1
        b = self.ruta2
        print(f"{a} || {b}")
        print('llamado en la linea 52')
 

App().mainloop()        
