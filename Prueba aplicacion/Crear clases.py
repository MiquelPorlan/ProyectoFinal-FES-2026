class Saludo:
    def __init__(self):
        print("¡Acabo de ser creado!")
    def hola():
        print('hola caracola')

#Saludo.hola
#Saludo.hola()

class Persona:
    def __init__(self, nombre): # __init__ se ejecuta solo cada vez que se crea un objeto. 
        self.nombre = nombre    # self. hace que la variable nombre se guarde en el objeto y no de forma local
        print (nombre + ' acaba de aparecer') 

    def saludar(self): 
        print("Hola, soy " + self.nombre)
class PersonaMuda:
    def __init__(self, nombre): # __init__ se ejecuta solo cada vez que se crea un objeto. 
        self.nombre = nombre    # self. hace que la variable nombre se guarde en el objeto y no de forma local
        print (nombre + ' acaba de aparecer') 

#    def saludar(self): 
#        print("Hola, soy " + self.nombre)

ana = Persona("Ana")
luis = PersonaMuda("Luis")

ana.saludar()
luis.saludar()


class Prueba:
    def mostrar(self):
        print("self es:", self)

a = Prueba()
b = Prueba()

print("a es:", a)
a.mostrar()
print("b es:", b)
b.mostrar()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def presentarse(self):
        print("Soy " + self.nombre + " y soy un " + self.raza)

rex = Perro("Rex", "pastor aleman")
rex.presentarse()