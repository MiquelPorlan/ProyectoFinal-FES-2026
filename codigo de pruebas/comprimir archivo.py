tablaEjemplo = [('H', 0), ('o', 10), ('l', 110), ('a', 1110)]
textEjemplo = "Hola"
textoComprimido = ''
lista =list(textEjemplo)

## comprimir texto ##

for i in lista:
    for caracter, indice in tablaEjemplo:
        if caracter == i:
            textoComprimido += str(indice)
print(textoComprimido) 

## descomprimir texto ## 

lista = list(textoComprimido)
textoDescomprimido = ''
n = 0
for i in lista:
    if i == '0':
        textoDescomprimido += tablaEjemplo[n][0]
        n = 0
    else:
        n += 1
print(textoDescomprimido)


            

       
    
