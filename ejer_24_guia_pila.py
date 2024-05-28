from pila import Stack

class PersonajeMarvel:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

    def get_nombre(self):
            return self.nombre

    def get_peliculas(self):
        return self.peliculas

    def __str__(self):
        return f"{self.nombre} ha participado en {self.peliculas} películas."
    
Personajes_marvel = [
PersonajeMarvel("Iron Man", 9),
PersonajeMarvel("Capitán América", 8),
PersonajeMarvel("Thor", 7),
PersonajeMarvel("Hulk", 7),
PersonajeMarvel("Black Widow", 7),
PersonajeMarvel("Hawkeye", 6),
PersonajeMarvel("Spider-Man", 6),
PersonajeMarvel("Doctor Strange", 3),
PersonajeMarvel("Rocket Raccoon", 5),
PersonajeMarvel("Ant-Man", 3),
PersonajeMarvel("Guardians of the Galaxy", 3),
PersonajeMarvel("Groot", 5)
]

stack_personajes = Stack()
stack_aux = Stack()


for personaje in Personajes_marvel:
    stack_personajes.push(personaje)

# while stack_personajes.size()>0:
#     print(stack_personajes.pop())

print()

pos = 0

while stack_personajes.size() > 0:
    pje = stack_personajes.pop()
    pos += 1
    if pje.get_nombre() == "Rocket Raccoon":
        print("el personaje se encontro en la pos: ", pos)
        stack_aux.push(pje)
    elif pje.get_nombre() == "Groot":
            print("el personaje se encontro en la pos: ", pos)
            stack_aux.push(pje)
    else:
         stack_aux.push(pje)

print()

# while stack_aux.size() > 0 :
#     print(stack_aux.pop())

print("Personajes con mas de 5 peliculas: ")

while stack_aux.size() > 0:
     pje = stack_aux.pop()
     if pje.get_peliculas() > 5:
          print(pje)
          stack_personajes.push(pje)
     else:
          stack_personajes.push(pje)

print ()

# while stack_personajes.size() > 0:
#      print(stack_personajes.pop())

print("Cantidad de peliculas en las que participo la viuda negra: ")

while stack_personajes.size() > 0:
     pje = stack_personajes.pop()
     if pje.get_nombre() == "Black Widow":
            print(pje.get_peliculas())
            stack_aux.push(pje)
     else:
            stack_aux.push(pje)

print()

print("Personajes cuyos nombres empiezan con C, D o G:")
while stack_aux.size() > 0:
    pje = stack_aux.pop()
    nombre = pje.get_nombre()
    if nombre.startswith("C") or nombre.startswith("D") or nombre.startswith("G"):
        print(nombre)
    stack_personajes.push(pje)
else:
     stack_personajes.push(pje)

print()

# while stack_personajes.size() > 0:
#      print(stack_personajes.pop())