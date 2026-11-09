from utils.lib1 import * 

## crear tabla ##

texto = leerArchivo("Archivos de prueba/Texto.txt")
tabla = contarCaracteres(texto)
tabla = crearIndices(tabla)

## comprimir texto ##

lista =list(texto)
textoComprimido = ''

for i in lista:
    for caracter, indice in tabla:
        if caracter == i:
            textoComprimido += str(indice)

