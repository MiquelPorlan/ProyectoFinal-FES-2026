
textEjemplo1= "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"
textEjemplo2= "Hola mundo"

# de momento solo Texto #

lista = list(textEjemplo1)
tabla = []
for c in set(lista):
    tabla.append((c, lista.count(c)))
    tabla.sort(key=lambda x: x[1],reverse=True)
print(tabla)

