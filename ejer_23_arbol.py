from arbol import BinaryTree

criaturas = [
    {"criatura": "Ceto", 
     "derrotado_por": None, 
     "descripcion": "Criatura primitiva del mar, personificación del peligro marino.",
     "capturada": None},
    {"criatura": "Tifón", 
     "derrotado_por": "Zeus", 
     "descripcion": "Gigante con cien cabezas de serpiente que lanzó una revuelta contra los dioses del Olimpo.",
     "capturada": None},
    {"criatura": "Equidna", 
     "derrotado_por": "Argos Panoptes", 
     "descripcion": "Mujer serpiente que es la madre de muchos de los monstruos mitológicos.",
     "capturada": None},
    {"criatura": "Dino", 
     "derrotado_por": None, 
     "descripcion": "Un monstruo con forma de serpiente, considerado como el ancestro de la hidra.",
     "capturada": None},
    {"criatura": "Pefredo", 
     "derrotado_por": None, 
     "descripcion": "Monstruo mitológico con aspecto de león, asociado con el miedo y la destrucción.",
     "capturada": None},
    {"criatura": "Enio", 
     "derrotado_por": None, 
     "descripcion": "Diosa de la guerra y la destrucción, que participaba en las batallas de los dioses y héroes.",
     "capturada": None},
    {"criatura": "Escila", 
     "derrotado_por": None, 
     "descripcion": "Monstruo marino con seis cabezas de serpiente que devoraba a los marineros.",
     "capturada": None},
    {"criatura": "Caribdis", 
     "derrotado_por": None, 
     "descripcion": "Monstruo marino que producía un gigantesco remolino para devorar barcos y marineros.",
     "capturada": None},
    {"criatura": "Euríale", 
     "derrotado_por": None, 
     "descripcion": "Una de las Górgonas, hermanas de Medusa, con serpientes en lugar de cabellos y mirada mortal.",
     "capturada": None},
    {"criatura": "Esteno", 
     "derrotado_por": None, 
     "descripcion": "Otra de las Górgonas, hermana de Medusa y Euríale, conocida por su aspecto terrorífico.",
     "capturada": None},
    {"criatura": "Medusa", 
     "derrotado_por": "Perseo", 
     "descripcion": "La Górgona más famosa, cuya mirada convierte en piedra a quien la observa.",
     "capturada": None},
    {"criatura": "Ladón", 
     "derrotado_por": "Heracles", 
     "descripcion": "Dragón de cien cabezas que custodiaba las manzanas doradas del Jardín de las Hespérides.",
     "capturada": None},
    {"criatura": "Águila del Cáucaso", 
     "derrotado_por": None, 
     "descripcion": "Águila gigante que devoraba el hígado de Prometeo cada día, castigado por robar el fuego.",
     "capturada": None},
    {"criatura": "Quimera", 
     "derrotado_por": "Belerofonte", 
     "descripcion": "Monstruo con la cabeza de león, cuerpo de cabra y cola de serpiente, que respiraba fuego.",
     "capturada": None},
    {"criatura": "Hidra de Lerna", 
     "derrotado_por": "Heracles", 
     "descripcion": "Serpiente acuática con múltiples cabezas que se regeneraban al ser cortadas.",
     "capturada": None},
    {"criatura": "León de Nemea", 
     "derrotado_por": "Heracles", 
     "descripcion": "León con una piel impenetrable, derrotado por Heracles como uno de sus trabajos.",
     "capturada": None},
    {"criatura": "Esfinge", 
     "derrotado_por": "Edipo", 
     "descripcion": "Criatura con cuerpo de león y cabeza de mujer que planteaba acertijos a los viajeros.",
     "capturada": None},
    {"criatura": "Dragón de la Cólquida", 
     "derrotado_por": None, 
     "descripcion": "Dragón que custodiaba el vellocino de oro en la Cólquida, con escamas doradas y mirada aterradora.",
     "capturada": None},
    {"criatura": "Cerbero", 
     "derrotado_por": None, 
     "descripcion": "Perro de tres cabezas que guardaba las puertas del inframundo, impidiendo que los muertos escaparan.",
     "capturada": None},
    {"criatura": "Cerda de Cromión",
      "derrotado_por": "Teseo", 
      "descripcion": "Jabalí gigante que aterrorizaba la región de Cromión, derrotado por el héroe Teseo.",
      "capturada": None},
    {"criatura": "Ortro", 
     "derrotado_por": "Heracles", 
     "descripcion": "Criatura no especificada, derrotada por el héroe Heracles en sus aventuras.",
     "capturada": None},
    {"criatura": "Toro de Creta", 
     "derrotado_por": "Teseo", 
     "descripcion": "Toro salvaje que causaba destrucción en Creta, capturado por el héroe Teseo.",
     "capturada": None},
    {"criatura": "Jabalí de Calidón", 
     "derrotado_por": "Atalanta", 
     "descripcion": "Jabalí monstruoso que fue cazado por una expedición de héroes liderada por Atalanta.",
     "capturada": None},
    {"criatura": "Carcinos", 
     "derrotado_por": None, 
     "descripcion": "Un monstruo en forma de cangrejo gigante que asistió a la Hidra de Lerna en su batalla contra Heracles.",
     "capturada": None},
    {"criatura": "Gerión", 
     "derrotado_por": "Heracles", 
     "descripcion": "Gigante de tres cuerpos que poseía un rebaño de ganado de oro, derrotado por Heracles.",
     "capturada": None},
    {"criatura": "Cloto", 
     "derrotado_por": None, 
     "descripcion": "Una de las Moiras que hilaba el hilo del destino de los humanos.",
     "capturada": None},
    {"criatura": "Láquesis", 
     "derrotado_por": None, 
     "descripcion": "Otra de las Moiras que medía la longitud del hilo del destino.",
     "capturada": None},
    {"criatura": "Átropos", 
     "derrotado_por": None, 
     "descripcion": "La última de las Moiras que cortaba el hilo del destino, determinando el final de la vida.",
     "capturada": None},
    {"criatura": "Minotauro de Creta", 
     "derrotado_por": "Teseo", 
     "descripcion": "Monstruo con cuerpo de hombre y cabeza de toro que vivía en el laberinto de Creta.",
     "capturada": None},
    {"criatura": "Harpías", 
     "derrotado_por": None, 
     "descripcion": "Seres con cuerpo de pájaro y rostro de mujer, que robaban comida y causaban estragos.",
     "capturada": None},
    {"criatura": "Argos Panoptes", 
     "derrotado_por": "Hermes", 
     "descripcion": "Gigante con cien ojos que custodiaba a Io, y que fue dormido y asesinado por Hermes.",
     "capturada": None},
    {"criatura": "Aves del Estínfalo", 
     "derrotado_por": None, 
     "descripcion": "Aves con plumas metálicas que lanzaban como flechas, derrotadas por Heracles.",
     "capturada": None},
    {"criatura": "Talos", 
     "derrotado_por": "Medea", 
     "descripcion": "Autómata de bronce que custodiaba la isla de Creta, derribado por Medea con magia.",
     "capturada": None},
    {"criatura": "Sirenas", 
     "derrotado_por": None, 
     "descripcion": "Criaturas marinas con canto seductor que atraían a los marineros a la perdición.",
     "capturada": None},
    {"criatura": "Pitón", 
     "derrotado_por": "Apolo", 
     "descripcion": "Serpiente gigante que habitaba el monte Parnaso, derrotada por Apolo en su ascenso al poder.",
     "capturada": None},
    {"criatura": "Cierva de Cerinea", 
     "derrotado_por": None, 
     "descripcion": "Cierva sagrada con cuernos de oro y pezuñas de bronce, capturada por Heracles.",
     "capturada": None},
    {"criatura": "Basilisco", 
     "derrotado_por": None, 
     "descripcion": "Serpiente con una mirada mortal que petrificaba a sus víctimas con solo mirarlas.",
     "capturada": None},
    {"criatura": "Jabalí de Erimanto", 
     "derrotado_por": None, 
     "descripcion": "Jabalí monstruoso que devastaba los campos de la región de Erimanto, cazado por Heracles.",
     "capturada": None}
]



tree_criaturas = BinaryTree()

for criatura in criaturas:  #ae 
    tree_criaturas.insert_node_creature(criatura['criatura'],criatura['derrotado_por'],criatura['descripcion'],
                                        criatura['capturada'])

tree_criaturas.inorden_criaturas()

pos = tree_criaturas.search("Talos")
if pos is not None:
     print(f"critura: {pos.value}, derrotado por: {pos.other_value}, descripción: {pos.description}")

print()

heroes_counter = tree_criaturas.contar_heroes()

top_3_heroes = heroes_counter.most_common(3) # guarda una lista de tuplas que contienen los nombres de los héroes o dioses que derrotaron la mayor cantidad de criaturas, junto con el número de criaturas que derrotaron

for heroe, count in top_3_heroes:
     print(f"{heroe}: {count} criaturas derrotadas")

print()

print("Criaturas derrotadas por Heracles: ")
tree_criaturas.defeated_by_heracles()

print()

print("Crituras sin derrotar: ")
tree_criaturas.undefeated()

pos_cerbero = tree_criaturas.search("Cerbero")
if pos_cerbero is not None:
     pos_cerbero.capturada = "Heracles"

pos_T_de_Creta = tree_criaturas.search("Toro de Creta")
if pos_T_de_Creta is not None:
     pos_T_de_Creta.capturada = "Heracles"

pos_C_Cerinea = tree_criaturas.search("Cierva de Cerinea")
if pos_C_Cerinea is not None:
     pos_C_Cerinea.capturada = "Heracles"

pos_Jabalí = tree_criaturas.search("Jabalí de Erimanto")
if pos_Jabalí is not None:
     pos_Jabalí.capturada = "Heracles"

# pos_2 = pos = tree_criaturas.search("Cerbero")
# if pos is not None:
#      print(f"critura: {pos.value}, capturada por: {pos.capturada}")

print()

tree_criaturas.search_by_coincidence("Heracles")

print()

tree_criaturas.delete_node("Basilisco")
tree_criaturas.delete_node("Sirenas")

pos_A_Estínfalo = tree_criaturas.search("Aves del Estínfalo")

if pos_A_Estínfalo is not None:
     pos_A_Estínfalo.other_value = "varias"

pos_Ladón = tree_criaturas.search("Ladón")
if pos_Ladón is not None:
     pos_Ladón.value = "Dragón Ladón"

tree_criaturas.by_level()

print()

print("criaturas capturadas por Heracles: ")
tree_criaturas.captured_by_heracles()