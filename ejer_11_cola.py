from cola import Queue

personajes_star_wars = [
    {
        "nombre": "Luke Skywalker",
        "planeta_natal": None,  #Tatooine
        "origen": "Humano, Jedi"
    },
    {
        "nombre": "Leia Organa",
        "planeta_natal": "Alderaan",
        "origen": "Humana, Princesa de Alderaan"
    },
    {
        "nombre": "Han Solo",
        "planeta_natal": None,  #Corellia
        "origen": "Humano, Contrabandista"
    },
    {
        "nombre": "Chewbacca",
        "planeta_natal": "Kashyyyk",
        "origen": "Wookiee, Contrabandista"
    },
    {
        "nombre": "Mace Windu",
        "planeta_natal": "Haruun Kal",
        "origen": "Humano, Maestro Jedi"  # Nuevo personaje
    },
    {
        "nombre": "Yoda",
        "planeta_natal": "unknown",
        "origen": "Yoda, Maestro Jedi"
    },
    {
        "nombre": "Obi-Wan Kenobi",
        "planeta_natal": "Stewjon",
        "origen": "Humano, Jedi"
    },
    {
        "nombre": "Darth Vader",
        "planeta_natal": "Tatooine",
        "origen": "Humano, Sith Lord"
    },
    {
        "nombre": "R2-D2",
        "planeta_natal": "Naboo",
        "origen": "Droide Astro"
    },
    {
        "nombre": "Jar Jar Binks",
        "planeta_natal": "Naboo",
        "origen": "Gungan, Senador"
    },
    {
        "nombre": "C-3PO",
        "planeta_natal": "Tatooine",
        "origen": "Droide Protocolo"
    },
    {
        "nombre": "Boba Fett",
        "planeta_natal": "Endor",
        "origen": "Mandaloriano, Cazarrecompensas"
    },
]

star_wars = Queue()
cola_aux = Queue()

for personaje in personajes_star_wars:
    star_wars.arrive(personaje)

print("Personajes del planeta Alderaan, Endor o Tatooine: ")

while star_wars.size() > 0:
    personaje = star_wars.attention()
    if personaje['planeta_natal'] == "Alderaan" or personaje['planeta_natal'] == "Endor" or personaje['planeta_natal'] == "Tatooine":
        print(personaje)
        cola_aux.arrive(personaje)
    else:
        cola_aux.arrive(personaje)

print()

# while cola_aux.size() > 0:
#     print(cola_aux.attention())

while cola_aux.size() > 0:
    personaje = cola_aux.attention()
    if personaje['nombre'] == "Luke Skywalker":
        personaje['planeta_natal'] = "Tatooine"
        star_wars.arrive(personaje)
    elif personaje['nombre'] == "Han Solo":
        personaje['planeta_natal'] = "Corellia"
        star_wars.arrive(personaje)
    else:
        star_wars.arrive(personaje)

while star_wars.size() > 0:
    personaje = star_wars.attention()
    if personaje["nombre"] == "C-3PO":
        pass
    else:
        cola_aux.arrive(personaje)

while cola_aux.size() > 0:
    personaje= cola_aux.attention()
    star_wars.arrive(personaje)

while star_wars.size() > 0:
    print(star_wars.attention())
