from lista import search,show_list,remove,by_name,by_año_aparicion

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
    "nombre": "Doctor Strange",
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
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas, usa traje."
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
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]

superheroe_eliminado = remove(super_heroes, "nombre", "Linterna Verde")

if superheroe_eliminado is not None:
    print(f"El superhéroe '{superheroe_eliminado['nombre']}' ha sido eliminado de la lista.")
else:
    print("El superhéroe 'Linterna Verde' no se encontró en la lista.")


indice_wolverine = search(super_heroes, "nombre", "Wolverine")


if indice_wolverine is not None:
    año_aparicion_wolverine = super_heroes[indice_wolverine]["año_aparicion"]
    print(f"El año de aparición de Wolverine es {año_aparicion_wolverine}.")
else:
    print("Wolverine no se encuentra en la lista.")


indice_dr_strange = search(super_heroes, "nombre", "Doctor Strange")

if indice_dr_strange is not None:
    super_heroes[indice_dr_strange]["casa_comic"] = "Marvel"
    print(f"La casa de cómics de Dr. Strange se ha actualizado a {super_heroes[indice_dr_strange]['casa_comic']}.")
else:
    print("Dr. Strange no se encuentra en la lista.")

print()

for heroe in super_heroes:
    if 'traje' in heroe['biografia'] or 'armadura' in heroe['biografia']:
        print(heroe['nombre'],heroe['biografia'])

print()

for heroe in super_heroes:
    if heroe['año_aparicion'] < 1963:
        print(heroe['nombre'],'-', heroe['casa_comic'])

print()

capitana_marvel = search(super_heroes,'nombre','Capitana Marvel')

if capitana_marvel is not None:
    print(super_heroes[capitana_marvel]['casa_comic'])
else:
    print('Capitana Marvel no se encuentra en la lista')

mujer_maravilla = search(super_heroes,'nombre','Wonder Woman')

if mujer_maravilla is not None:
    print(super_heroes[mujer_maravilla]['casa_comic'])
else:
    print('La Mujer Maravilla no se encuentra en la lista')

print()

flash = search(super_heroes,'nombre','Flash')

if flash is not None:
    print(super_heroes[flash])
else:
    print('Flash no se encuentra en la lista')


star_lord = search(super_heroes,'nombre','Star-Lord')

if star_lord is not None:
    print(super_heroes[star_lord])
else:
    print('Star Lord no se encuentra en la lista')

print()

for heroe in super_heroes:
    if heroe["nombre"].startswith(('B','S','M')):
        print(heroe["nombre"])

print()

cont_dc = 0
cont_marvel = 0

for heroe in super_heroes:
    if heroe["casa_comic"] == 'Marvel Comics':
        cont_marvel += 1
    else:
          if heroe["casa_comic"] == 'DC Comics':
                cont_dc += 1
                
print(f"la cantidad de personajes de DC es {cont_dc}")
print(f"la cantidad de personajes de Marvel es {cont_marvel}")
