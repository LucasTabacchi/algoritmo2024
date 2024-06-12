from random import randint, choice

tipos = ['Fuego', 'Agua', 'Planta', 'Eléctrico', 'Roca', 'Psíquico']

# Funciones hash
def hash_tipos(pokemon):
    return pokemon.split('-')[0].split(',')

def hash_ultimo_digito(pokemon):
    return int(pokemon.split('-')[2][-1])

    # return pokemon.split('-')[2][-1]

def hash_nivel(pokemon):
    return int(pokemon.split('-')[1]) // 10

def cargar_pokemon(pokemon):
    numero = int(pokemon.split('-')[2])
    tipos = pokemon.split('-')[0].split(',')
    nivel = int(pokemon.split('-')[1]) // 10

    for tipo in tipos:
        tabla_tipo[tipo].append(pokemon)
    tabla_nivel[hash_nivel(pokemon)].append(pokemon)
    tabla_numero[hash_ultimo_digito(pokemon)].append(pokemon)

tabla_tipo = {tipo: [] for tipo in tipos}
tabla_nivel = {i: [] for i in range(10)}
tabla_numero = {i: [] for i in range(10)}
# tabla_numero = {str(i): [] for i in range(10)}


for i in range(10):
    if randint(0, 1) == 0:
        pokemon = f'{choice(tipos)}-{randint(1,99)}-{randint(1000,9999)}'
    else:
        tipo1, tipo2 = choice(tipos), choice(tipos)
        while tipo1 == tipo2:
            tipo2 = choice(tipos)
        pokemon = f'{tipo1},{tipo2}-{randint(1,99)}-{randint(1000,9999)}'
    
    tipos_pokemon = hash_tipos(pokemon)
    nivel = hash_nivel(pokemon)
    ultimo_digito = hash_ultimo_digito(pokemon)

    for tipo in tipos_pokemon:
        tabla_tipo[tipo].append(pokemon)

    tabla_nivel[nivel].append(pokemon)
    tabla_numero[ultimo_digito].append(pokemon)

pokemon_1 = 'Fuego-50-123'
# pokemon_2 = 'Fuego,Agua-50-123'

cargar_pokemon(pokemon_1)

print("Tabla por tipo:")
for tipo in tabla_tipo:
    print(f"{tipo}: {tabla_tipo[tipo]}")

print()

print("Tabla por nivel:")
for nivel in tabla_nivel:
    print(f"{nivel * 10}-{(nivel + 1) * 10 - 1}: {tabla_nivel[nivel]}")

print()

print("Tabla por último dígito del número:")
for numero in tabla_numero:
    print(f"{numero}: {tabla_numero[numero]}")

print("-")

# print("Pokémons cuyos números terminan en 3:")
# for pokemon in tabla_numero[3]:
#     print(pokemon)

# print("Pokémons cuyos números terminan en 7:")
# for pokemon in tabla_numero[7]:
#     print(pokemon)

# print("Pokémons cuyos números terminan en 9:")
# for pokemon in tabla_numero[9]:
#     print(pokemon)

print("Pokémons cuyos números terminan en 3:")
list_3 = tabla_numero.get(3, [])
print(list_3)

print("Pokémons cuyos números terminan en 7:")
list_7 = tabla_numero.get(7, [])
print(list_7)

print("Pokémons cuyos números terminan en 9:")
list_9 = tabla_numero.get(9, [])
print(list_9)

print("-")

print("Pokémons cuyos niveles son múltiplos de 2:")
for lista in tabla_nivel.values():
    for pokemon in lista:
        nivel = int(pokemon.split('-')[1])
        if nivel % 2 == 0:
            print(pokemon)

print("Pokémons cuyos niveles son múltiplos de 5:")
for lista in tabla_nivel.values():
    for pokemon in lista:
        nivel = int(pokemon.split('-')[1])
        if nivel % 5 == 0:
            print(pokemon)

print("Pokémons cuyos niveles son múltiplos de 10:")
for lista in tabla_nivel.values():
    for pokemon in lista:
        nivel = int(pokemon.split('-')[1])
        if nivel % 10 == 0:
            print(pokemon)

print("-")

tipos_especificos = ['Acero', 'Fuego', 'Eléctrico', 'Hielo']
# print("Pokémons de los tipos Acero, Fuego, Eléctrico e Hielo:")
# for tipo in tipos_especificos:
#     if tipo in tabla_tipo:
#         print(f"Tipo {tipo}:")
#         for pokemon in tabla_tipo[tipo]:
#             print(pokemon)
#     else:
#         print(f"\nTipo {tipo}: No hay Pokémon de este tipo.")


for tipo in tipos_especificos:
    if tipo in tabla_tipo.keys():
        print(f"Tipo {tipo}:")
        for pokemon in tabla_tipo[tipo]:
            print(pokemon)
    else:
        print(f"No hay Pokémon del tipo {tipo}")
