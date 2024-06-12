from lista import by_name, show_list, search, show_list_list, by_temp, remove
from random import choice


entrenadores = [
    {'nombre': 'Ash Ketchum', 'torneos_ganados': 3, 'batallas_perdidas': 50, 'batallas_ganadas': 200},
    {'nombre': 'Misty', 'torneos_ganados': 1, 'batallas_perdidas': 20, 'batallas_ganadas': 100},
    {'nombre': 'Brock', 'torneos_ganados': 2, 'batallas_perdidas': 30, 'batallas_ganadas': 120},
    {'nombre': 'Gary Oak', 'torneos_ganados': 4, 'batallas_perdidas': 10, 'batallas_ganadas': 180},
    {'nombre': 'Serena', 'torneos_ganados': 1, 'batallas_perdidas': 15, 'batallas_ganadas': 90},
]

pokemons = [
    {'nombre': 'Charizard', 'nivel': 65, 'tipo': 'Fuego', 'subtipo': 'Volador'},
    {'nombre': 'Bulbasaur', 'nivel': 45, 'tipo': 'Planta', 'subtipo': 'Veneno',},
    {'nombre': 'Jigglypuff', 'nivel': 35, 'tipo': 'Normal', 'subtipo': 'Hada'},
    {'nombre': 'Gyarados', 'nivel': 70, 'tipo': 'Agua', 'subtipo': 'Volador'},
    {'nombre': 'Charizard', 'nivel': 65, 'tipo': 'Fuego', 'subtipo': 'Volador'},
    {'nombre': 'Gengar', 'nivel': 60, 'tipo': 'Fantasma', 'subtipo': 'Veneno'},
    {'nombre': 'Jigglypuff', 'nivel': 35, 'tipo': 'Normal', 'subtipo': 'Hada'},
    {'nombre': 'Bulbasaur', 'nivel': 45, 'tipo': 'Planta', 'subtipo': 'Veneno'},
    {'nombre': 'Bulbasaur', 'nivel': 45, 'tipo': 'Planta', 'subtipo': 'Veneno'},
    {'nombre': 'Tyrantrum', 'nivel': 45, 'tipo': 'Normal', 'subtipo': 'Fantasma'},
    {'nombre': 'Terrakion', 'nivel': 45, 'tipo': 'Normal', 'subtipo': 'Fantasma'},
    {'nombre': 'Wingull', 'nivel': 45, 'tipo': 'Normal', 'subtipo': 'Fantasma'}, 
]

lista_entrenadores = []

names = ["Ash Ketchum","Misty","Brock","Gary Oak","Serena"] 

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('El entrenador no esta en la lista')

lista_entrenadores.sort(key=by_name)

show_list_list('Entrenador','Pokemons',lista_entrenadores)

def cantidad_pokemons(list_entrenadores, nombre_entrenador):
    pos = search(list_entrenadores, 'nombre', nombre_entrenador)
    if pos is not None:
        print(f'los lista de pokemones del entrenador {nombre_entrenador} es: ')
        print(list_entrenadores[pos]['sublist'])
    else:
        return print("el entrenador no esta en la lista")
    
cantidad_pokemons(lista_entrenadores,'Brock')

print()

print('entrenador con mas de 3 torneos ganados')
for e in lista_entrenadores:
    if e['torneos_ganados'] > 3:
        print(e)

print('-') 
        
mayor = None
max_torneos_ganados = 0

for entrenador in lista_entrenadores:
    if entrenador['torneos_ganados'] > max_torneos_ganados:
        mayor = entrenador
        max_torneos_ganados = entrenador['torneos_ganados']
        nombre_e = entrenador['nombre']

if mayor is not None:
    max_nivel = 0
    pokemon_mayor_nivel = None
    for pokemon in mayor['sublist']:
        if pokemon['nivel'] > max_nivel:
            pokemon_mayor_nivel = pokemon


print(f'el entrenador con mas torneos ganados es {nombre_e} y el pokemon que mayor nivel que tiene es {pokemon_mayor_nivel}')


def datos_entrenador(title, subtitle, entrenador):
    print()
    print(f"{title}")
    if entrenador:
        print(f" {entrenador['nombre']}, Batallas ganadas: {entrenador['batallas_ganadas']}, Batallas perdidas: {entrenador['batallas_perdidas']}, Torneos ganados: {entrenador['torneos_ganados']}")
        print(f"    {subtitle}")
        for pokemon in entrenador['sublist']:
            print(f"    {pokemon['nombre']}, Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo: {pokemon.get('subtipo', 'Ninguno')}")
    else:
        print("El entrenador no existe o no tiene Pokémons.")


pos = search(lista_entrenadores, 'nombre', 'Misty')
if pos is not None:
    datos_entrenador('Datos del Entrenador', 'Pokémons', lista_entrenadores[pos])
else:
    print("El entrenador no se encontró en la lista.")

print()

for entrenador in lista_entrenadores:
    if e['batallas_ganadas'] > 79: 
        print(entrenador)

print("-")

t_pokemons = ['Agua', 'Fuego', 'Volador', 'Planta']
print("Entrenadores que tienen pokemones de tipo fuego, planta, volador o agua: ")

entrenadores_vistos = set()

for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['tipo'] in t_pokemons or pokemon['subtipo'] in t_pokemons:
            if entrenador['nombre'] not in entrenadores_vistos:
                print(f"{entrenador['nombre']}")
                entrenadores_vistos.add(entrenador['nombre'])

print('-')

# nombre_entrenador = input('ingrese el nombre del entrenador') 
# suma_nivel = 0
# cant = 0
# promedio = None

# for entrenador in lista_entrenadores:
#     if entrenador['nombre'] == nombre_entrenador:
#         for e in entrenador['sublist']:
#             suma_nivel += e['nivel']
#             cant += 1
#         promedio = (suma_nivel / cant) 

# print(f'el promedio de nivel de los pokemones del {nombre_entrenador} es {promedio}')

def contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    contador = 0
    for entrenador in entrenadores:
        pokemons_vistos = set()  
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] == nombre_pokemon:
                if pokemon['nombre'] not in pokemons_vistos:
                    pokemons_vistos.add(pokemon['nombre'])
                    contador += 1
                    break
    return contador

nombre_pokemon = 'Bulbasaur'  
cantidad_entrenadores = contar_entrenadores_con_pokemon(lista_entrenadores, nombre_pokemon)
print(f"El Pokémon {nombre_pokemon} está en posesión de {cantidad_entrenadores} entrenadores.")

print("-")

def mostrar_entrenadores_con_pokemons_repetidos(entrenadores):
    entrenadores_con_repetidos = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon['nombre'] for pokemon in entrenador['sublist']]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):  
            entrenadores_con_repetidos.append(entrenador['nombre'])
    return entrenadores_con_repetidos
            
entrenadores_repetidos = mostrar_entrenadores_con_pokemons_repetidos(lista_entrenadores)

print("entrenadores con pokemons repetidos: ")

for nombre_entrenador in entrenadores_repetidos:
    print(nombre_entrenador)

print("-")


def p_tyrantrum_terrakion_wingull(entrenadores):
    lista_pokemones = ["Tyrantrum","Terrakion","Wingull"]
    list_entrenadores = set()
    for entrenador in entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] in lista_pokemones :
                list_entrenadores.add(entrenador['nombre'])

    return list_entrenadores

entrenadores_con_pokemon = p_tyrantrum_terrakion_wingull(lista_entrenadores)
for nombre_entrenador in entrenadores_con_pokemon:
    print(nombre_entrenador)            

print("-")

def buscar_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    entrenador_encontrado = False
    pokemon_encontrado = False

    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            entrenador_encontrado = True
            for pokemon in entrenador['sublist']:
                if pokemon['nombre'] == nombre_pokemon:
                    pokemon_encontrado = True
                    print(f"El entrenador {entrenador['nombre']} tiene al Pokémon {pokemon['nombre']}.")
                    
            if not pokemon_encontrado:
                print(f"El entrenador {nombre_entrenador} no tiene al Pokémon {nombre_pokemon}.")
            break

    if not entrenador_encontrado:
        print(f"No se encontró al entrenador {nombre_entrenador}.")

nom_pokemon = "Charizard"
nom_ent = "Misty"

buscar_pokemon(lista_entrenadores,nom_ent,nom_pokemon)