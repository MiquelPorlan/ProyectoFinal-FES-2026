def leerArchivo(ruta):
    with open(ruta, 'r') as file:
        texto = file.read()
        return texto

def contarCaracteres(texto):
    lista = list(texto)
    tabla = []
    for c in set(lista):
        tabla.append((c,lista.count(c)))
    tabla.sort(key=lambda x: x[1],reverse=True)
    return tabla

def crearIndices(tabla):
    for i in range(len(tabla)):
        indice = ""
        for j in range(0, i):
            indice += "1"
        indice += "0"
        tabla[i]=(tabla[i][0],indice)
    return tabla