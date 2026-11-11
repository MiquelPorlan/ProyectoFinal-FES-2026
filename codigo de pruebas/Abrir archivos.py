from pathlib import Path

Origen = Path("Archivos de prueba/imagen prueba.webp")


with open(Origen, 'rb') as f2:
    T2 = str(f2.read())

print(T2)