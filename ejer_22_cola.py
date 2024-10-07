from cola import Queue

personajes_mcu = [
    {
        "nombre_personaje": "Tony Stark",
        "superheroe": "Iron Man",
        "genero": "M"
    },
    {
        "nombre_personaje": "Steve Rogers",
        "superheroe": "Capitán América",
        "genero": "M"
    },
    {
        "nombre_personaje": "Natasha Romanoff",
        "superheroe": "Black Widow",
        "genero": "F"
    },
    {
        "nombre_personaje": "Bruce Banner",
        "superheroe": "Hulk",
        "genero": "M"
    },
    {
        "nombre_personaje": "Carol Danvers",
        "superheroe": "Captain Marvel",
        "genero": "F"
    },
    {
        "nombre_personaje": "Thor Odinson",
        "superheroe": "Thor",
        "genero": "M"
    },
    {
        "nombre_personaje": "Wanda Maximoff",
        "superheroe": "Scarlet Witch",
        "genero": "F"
    },
    {
        "nombre_personaje": "T'Challa",
        "superheroe": "Black Panther",
        "genero": "M"
    },
    {
        "nombre_personaje": "Peter Parker",
        "superheroe": "Spider-Man",
        "genero": "M"
    },
    {
        "nombre_personaje": "Stephen Strange",
        "superheroe": "Doctor Strange",
        "genero": "M"
    },
    {
        "nombre_personaje": "Hope van Dyne",
        "superheroe": "The Wasp",
        "genero": "F"
    },
    {
        "nombre_personaje": "Scott Lang",
        "superheroe": "Ant-Man",
        "genero": "M"
    },
    {
        "nombre_personaje": "Clint Barton",
        "superheroe": "Hawkeye",
        "genero": "M"
    },
    {
        "nombre_personaje": "Sam Wilson",
        "superheroe": "Falcon",
        "genero": "M"
    },
    {
        "nombre_personaje": "Gamora",
        "superheroe": "Gamora",
        "genero": "F"
    }
]

cola_marvel = Queue()
cola_aux = Queue()  

for personaje in personajes_mcu:
    cola_marvel.arrive(personaje)

print("Nombre del personaje de la superhéroe Capitana Marvel: ")
while cola_marvel.size() > 0:
    personaje = cola_marvel.attention()
    if personaje['superheroe'] == "Captain Marvel":
        print(personaje['nombre_personaje'])
        cola_aux.arrive(personaje)
    else:
        cola_aux.arrive(personaje)

print()

print("Personajes femeninos: ")
while cola_aux.size() > 0:
    personaje = cola_aux.attention()
    if personaje['genero'] == "F":
        print(personaje)
        cola_marvel.arrive(personaje)
    else:
        cola_marvel.arrive(personaje)

print()

print("Personajes masculinos: ")
while cola_marvel.size() > 0:
    personaje = cola_marvel.attention()
    if personaje['genero'] == "M":
        print(personaje)
        cola_aux.arrive(personaje)
    else:
        cola_aux.arrive(personaje)

print()

print("Nombre del superhéroe del personaje Scott Lang: ")
while cola_aux.size() > 0:
    personaje = cola_aux.attention()
    if personaje['nombre_personaje'] == "Scott Lang":
        print(personaje['superheroe'])
        cola_marvel.arrive(personaje)
    else:
        cola_marvel.arrive(personaje)

print()

print("Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S")
while cola_marvel.size() > 0:
    personaje = cola_marvel.attention()
    if personaje['nombre_personaje'].startswith('S') or personaje['superheroe'].startswith('S'):
        print(personaje)
        cola_aux.arrive(personaje)
    else:
        cola_aux.arrive(personaje)

print()
print("Nombre del superhéroe del personaje Carol Danvers: ")
while cola_aux.size() > 0:
    personaje = cola_aux.attention()
    if personaje['nombre_personaje'] == "Carol Danvers":
        print(personaje['superheroe'])
        cola_marvel.arrive(personaje)
    else:
        cola_marvel.arrive(personaje)

print()

while cola_marvel.size() > 0:
    print(cola_marvel.attention())

