from arbol import BinaryTree
from cola import Queue
from random import randint

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Roctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    'villano': True,
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Thanos",
    'villano': True
  },
  {
    "nombre": "Loctor Doom",
    'villano': True
  },
  {
    "nombre": "Green Golbing",
    'villano': True
  }
]

tree = BinaryTree()

for personaje in super_heroes:  #a
    is_hero = False if 'villano' in personaje else True
    tree.insert_node(personaje['nombre'], {'is_hero': is_hero})

# tree.inorden()
print("villanos ordenados alfabéticmanete: ")
tree.inorden_villanos() #b
print()
print("superhéroes que comienzan con c: ")
tree.inorden_superheros_start_with('C') #c
print()
print("la cantidad de superhéroes es: ")
print(tree.contar_super_heroes()) #d


pos = tree.search('Roctor Strange')  #e
if pos is not None:
      pos.value = 'Doctor Strange'

print()
print("listado de superhéroes en forma descendente: ")
tree.inorden_superheroes_descendente() #f

print()

heroes_tree = BinaryTree() #g
villains_tree = BinaryTree()

tree.generar_bosque(heroes_tree, villains_tree)

print("Superhéroes:")
heroes_tree.inorden()

print()

print("Villanos:")
villains_tree.inorden()

print("-------")




# #4

# hijo_derecho_de_Wolverine = tree.search_nd('Wolverine')
# if hijo_derecho_de_Wolverine is not None:
#     print(f"Hijo derecho de Wolverine: {hijo_derecho_de_Wolverine.value}")
# else:
#     print("Wolverine no tiene hijo derecho")


# hijo_izquierdo = tree.search_ni('Wolverine')
# if hijo_izquierdo is not None:
#     print(f"El hijo izquierdo de Wolverine es: {hijo_izquierdo.value}")
# else:
#     print("Wolverine no tiene hijo izquierdo.")

# print("-----")

# # print(tree.get_left_child("Wolverine"))
# # print(tree.get_right_child("Wolverine"))







tree_numeros = BinaryTree()

for i in range(11):
      tree_numeros.insert_node(randint(0,10))

tree_numeros.inorden()
print("-")
# tree_numeros.postorden()
# print("-")
# tree_numeros.preorden()

numero_buscado = tree_numeros.search(10)

if numero_buscado is not None:
      print("el numero buscado esta en la lista")
else:
      print("no se encuentra en la lista")

left_height = tree_numeros.height(tree_numeros.root.left)
right_height = tree_numeros.height(tree_numeros.root.right)
 
print(f"la altura izquierda es {left_height}")
print(f"la altura derecha es {right_height}")


# print(tree_numeros.contar_ocurrencias(3))

print()


tree.proximity_search('La')

value_to_delete = 'La Alforcha Humana'
delete_value, extra_info = tree.delete_node(value_to_delete)
print('eliminado', delete_value, extra_info)
new_name = 'La Antorcha Humana'
extra_info['nombre'] = new_name
tree.insert_node(new_name, extra_info)
tree.proximity_search('La')
pos = tree.search('La Antorcha Humana')
if pos:
    print('encontrado', pos.other_value)

print()
tree.proximity_search('La')
