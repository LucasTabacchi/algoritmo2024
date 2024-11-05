from arbol import BinaryTree

pokemons = [
    {
        "nombre": "Pikachu",
        "numero": 25,
        "tipos": ["Eléctrico"]
    },
    {
        "nombre": "Bulbasaur",
        "numero": 1,
        "tipos": ["Planta", "Veneno"]
    },
    {
        "nombre": "Charmander",
        "numero": 4,
        "tipos": ["Fuego"]
    },
    {
        "nombre": "Squirtle",
        "numero": 7,
        "tipos": ["Agua"]
    },
    {
        "nombre": "Gengar",
        "numero": 94,
        "tipos": ["Fantasma", "Veneno"]
    },
    {
        "nombre": "Mewtwo",
        "numero": 150,
        "tipos": ["Psíquico"]
    },
    {
        "nombre": "Lucario",
        "numero": 448,
        "tipos": ["Lucha", "Acero"]
    },
    {
        "nombre": "Greninja",
        "numero": 658,
        "tipos": ["Agua", "Siniestro"]
    },
    {
        "nombre": "Eevee",
        "numero": 133,
        "tipos": ["Normal"]
    },
    {
        "nombre": "Togekiss",
        "numero": 468,
        "tipos": ["Hada", "Volador"]
    },
    {
        "nombre": "Zygarde",
        "numero": 718,
        "tipos": ["Dragón", "Tierra"]
    },
    {
        "nombre": "Cinderace",
        "numero": 815,
        "tipos": ["Fuego"]
    },
    {
        "nombre": "Corviknight",
        "numero": 823,
        "tipos": ["Volador", "Acero"]
    },
    {
        "nombre": "Skwovet",
        "numero": 819,
        "tipos": ["Normal"]
    },
    {
        "nombre": "Alakazam",
        "numero": 65,
        "tipos": ["Psíquico"]
    },
    {
        "nombre": "Snorlax",
        "numero": 143,
        "tipos": ["Normal"]
    },
    {
        "nombre": "Dragonite",
        "numero": 149,
        "tipos": ["Dragón", "Volador"]
    },
    {
        "nombre": "Gardevoir",
        "numero": 282,
        "tipos": ["Psíquico", "Hada"]
    },
        {
        "nombre": "Jolteon",
        "numero": 135,
        "tipos": ["Eléctrico"]
    },
    {
        "nombre": "Lycanroc",
        "numero": 745,
        "tipos": ["Roca"]
    },
    {
        "nombre": "Tyrantrum",
        "numero": 697,
        "tipos": ["Roca", "Dragón"]
    }
]


nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

# Inserción en los árboles
for pokemon in pokemons:
    nombre_tree.insert_node(pokemon["nombre"],pokemon)
    numero_tree.insert_node(pokemon["numero"],pokemon)
    for tipo in pokemon["tipos"]:
        tipo_tree.insert_node(tipo,pokemon)

search_term = "bul"
nombre_tree.search_by_coincidence_pok(search_term)

search_term_num = "71"
numero_tree.search_by_proximity_num_pok(search_term_num)
print()
tipos_a_mostrar = ["Agua", "Fuego", "Planta", "Eléctrico"]
tipo_tree.mostrar_pokemon_por_tipo(tipos_a_mostrar)

print()

numero_tree.listado_ascendente_por_numero_nombre()
print()
nombre_tree.by_level()
print()

pos_jolteon = nombre_tree.search("Jolteon")
if pos_jolteon is not None:
    print("información del pokemón Jolteon:")
    print(pos_jolteon.other_value)

pos_lycanroc = nombre_tree.search("Lycanroc")
if pos_lycanroc is not None:
    print("información del pokemón Lycanroc:")
    print(pos_lycanroc.other_value)

pos_tyrantrum = nombre_tree.search("Tyrantrum")
if pos_tyrantrum is not None:
    print("información del pokemón Tyrantrum:")
    print(pos_tyrantrum.other_value)

print()

electrico_count = tipo_tree.contar_por_tipos("Eléctrico")
print(f"Cantidad de Pokémon de tipo Eléctrico: {electrico_count}")

acero_count = tipo_tree.contar_por_tipos("Acero")
print(f"Cantidad de Pokémon de tipo Acero: {acero_count}")


