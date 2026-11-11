with open('Archivos de prueba/imagen prueba.webp', 'rb') as file:
    prueba = file.read()

with open('Archivos de prueba/Archivo comprimido.txt', 'wb') as file:
    file.write(prueba)