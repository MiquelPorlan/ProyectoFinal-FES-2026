tablaEjemplo = [(' ', 7), ('a', 5), ('l', 4), ('o', 4), ('i', 3), ('e', 3), ('n', 2), ('c', 2), ('s', 2), ('b', 1), ('L', 1), ('g', 1), ('x', 1), ('t', 1), ('r', 1), ('p', 1)]


for i in range(len(tablaEjemplo)):
    indice = ""
    for j in range(0, i):
        indice += "1"
    indice += "0"
    tablaEjemplo[i]=(tablaEjemplo[i][0],indice)    
                
print (tablaEjemplo)

