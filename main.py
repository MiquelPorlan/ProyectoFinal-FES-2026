from utils.lib1 import * 

texto = leerArchivo("Archivos de prueba/Texto.txt")
tabla = contarCaracteres(texto)
tabla = crearIndices(tabla)
print(tabla)