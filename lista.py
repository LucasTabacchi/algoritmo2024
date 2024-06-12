# lista_de_elementos = [1, 20, 5, 67, 3, 4, -1]

# #! insertar con posicion
# lista_de_elementos.insert(2, 99)
# #! insertar sin posicion
# lista_de_elementos.append(123)

# #! eliminar un elemento de la lista (suponiendo valores unicos y dato simple)
# try:
#     lista_de_elementos.remove(101)
# except ValueError:
#     print('el elemento a eliminar no esta en la lista')
# if 67 in lista_de_elementos:
#     print('eliminar elemento')
#     lista_de_elementos.remove(67)
# else:
#     print('el elemento a eliminar no esta en la lista')

# #! tamanio
# print(len(lista_de_elementos))

# #! ordenar elementos simples
# lista_de_elementos.sort()

# #! busqueda elementos simples
# try:
#     print('posicion', lista_de_elementos.index(20))
# except ValueError:
#     print('el elemento que busca no esta en la lista')

# #! barrido
# print("Listado")
# for elemento in lista_de_elementos:
#     print(elemento)

# personajes_star_wars = [
#     {'nombre': 'Luke Skywalker', 'especie': 'Humano', 'altura': 172},
#     {'nombre': 'Princesa Leia', 'especie': 'Humano', 'altura': 150},
#     {'nombre': 'Han Solo', 'especie': 'Humano', 'altura': 180},
#     {'nombre': 'Darth Vader', 'especie': 'Humano', 'altura': 202},
#     {'nombre': 'Yoda', 'especie': 'Desconocida', 'altura': 66},
#     {'nombre': 'Obi-Wan Kenobi', 'especie': 'Humano', 'altura': 182},
#     {'nombre': 'Chewbacca', 'especie': 'Wookiee', 'altura': 228},
#     {'nombre': 'R2-D2', 'especie': 'Droide', 'altura': 96},
#     {'nombre': 'C-3PO', 'especie': 'Droide', 'altura': 167},
#     {'nombre': 'Padmé Amidala', 'especie': 'Humano', 'altura': 165}
# ]

# nuevo_personaje = {'nombre': 'Boba Fett', 'especie': 'Humano', 'altura': 178}
#! insertar con posicion
# personajes_star_wars.insert(8, nuevo_personaje)
#! insertar sin posicion
# nuevo_personaje_2 = {'nombre': 'Mace Windu', 'especie': 'Humano', 'altura': 190}
# personajes_star_wars.append(nuevo_personaje_2)

#! tamanio
# print(len(personajes_star_wars))

#! criterios de orden
def by_name(item):
    return item['nombre']

def by_hegiht(item):
    return item['altura']

def by_año_aparicion(item):
    return item['año_aparicion']

def by_house(item):
    return item['casa_comic']+item['nombre']

def by_temp(item):
    return item['temp']


#! ordenar elementos simples
# personajes_star_wars.sort(key=by_hegiht)

#! busqueda elementos simples
# try:
#     print('posicion', personajes_star_wars.index('Yoda'))
# except ValueError:
#     print('el elemento que busca no esta en la lista')

#! barrido
# print("Listado")
# for elemento in personajes_star_wars:
#     print(elemento['nombre'], elemento['especie'], elemento['altura'])


# # ejercicio_1
# cont = 0
# for elemento in personajes_star_wars:
#     print(elemento['nombre'], elemento['especie'], elemento['altura'])
#     cont +=1

# print(f'los cantidad de nodos de la lista es {cont}')

# #ejercicio_2
# lista_de_caracteres = ['a','b','d','t','z','i','R','Y']
# vocales = "aeiouAEIOU"
# lista_sin_vocales = []

# for caracter in lista_de_caracteres:
#     if caracter not in vocales:
#         lista_sin_vocales.append(caracter)

# print(lista_sin_vocales)

# #ejercicio_3
# lista_num= [2,3,6,7,9,10,13,23,25]
# lista_par = []
# lista_impar = []

# for element in lista_num:
#     if element % 2 == 0: 
#         lista_par.append(element)
#     else:
#         lista_impar.append(element)

# print(lista_par)
# print(lista_impar)

# #ejercicio_4

# lista = ['auto', 'computadora', 'casa', 'parlante']

# palabra = "sillon"

# # Encontrar el índice del elemento 'casa'
# indice_elemento = lista.index('parlante')

# # Reemplazar 'casa' por 'sillon'
# lista[indice_elemento] = palabra

# print(lista)

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

# print(f'Yoda esta en la posicion {search(personajes_star_wars, criterio, buscado)}')

#! eliminar un elemento de la lista
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

# eliminar = 'R2-D2'
# result_delete = remove(personajes_star_wars, criterio, eliminar)
# print(f'Eliminar {eliminar} resultado: {result_delete}')

#! barrido
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

# def show_list_list(title, subtitle, list_values):
#     print()
#     print(f"{title}")
#     for index, elemento in enumerate(list_values):
#         print(index, elemento['nombre'], elemento['id'])
#         print(f"    {subtitle}")
#         for second_index, second_element in enumerate(elemento['sublist']):
#             print('    ', second_index, second_element)
#     print()

def show_list_list(title, subtitle, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento['nombre'])
        print(f"    {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print('    ', second_index, second_element)
    print()
