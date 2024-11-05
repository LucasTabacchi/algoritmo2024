from grafo import Graph
from random import sample, randint
from collections import Counter

# Inicializamos el grafo
grafo = Graph(dirigido=True)

# Generamos 15 vértices aleatorios y los insertamos en el grafo
vertices = sample(range(1, 101), 15)  # 15 números únicos entre 1 y 100
for vertice in vertices:
    grafo.insert_vertice(vertice)

# grafo.show_graph()

# Creamos un conjunto para almacenar aristas ya insertadas (evita repeticiones)
aristas_insertadas = set()

# Generamos 30 aristas no repetidas
while len(aristas_insertadas) < 10:
    origen, destino = sample(vertices, 2)  # Seleccionamos dos vértices al azar
    if (origen, destino) not in aristas_insertadas and (destino, origen) not in aristas_insertadas:
        peso = randint(1, 100)  # Peso aleatorio entre 1 y 20
        grafo.insert_arista(origen, destino, peso)
        aristas_insertadas.add((origen, destino))  # Agregamos la arista al conjunto

grafo.show_graph()

print()


# vertices_a_eliminar = set()

#     # Verificar cada vértice
# for nodo in grafo.elements:
#      if len(nodo['aristas']) == 0:  # No tiene aristas salientes
#             vertices_a_eliminar.add(nodo['value'])

               
# for valor in vertices_a_eliminar:
#     grafo.delete_vertice(valor)


vertices_a_eliminar = []
for nodo in grafo.elements: # eliminar vertices aislados grafo dirigido
        # Primero verificamos que no tenga aristas salientes
        if len(nodo['aristas']) == 0:
            valor_nodo = nodo['value']
            tiene_aristas_entrantes = False
            
            # Verificamos si algún otro nodo tiene una arista hacia este nodo
            for otro_nodo in grafo.elements:
                if otro_nodo['value'] != valor_nodo:  # No revisamos el mismo nodo
                    for arista in otro_nodo['aristas']:
                        if arista['value'] == valor_nodo:
                            tiene_aristas_entrantes = True
                            break
                    if tiene_aristas_entrantes:
                        break
            
            # Si no tiene aristas entrantes ni salientes, lo marcamos para eliminar
            if not tiene_aristas_entrantes:
                vertices_a_eliminar.append(valor_nodo)

for vertice in vertices_a_eliminar:
        grafo.delete_vertice(vertice)
                     

grafo.show_graph()


max_aristas = 0
nodos_maximos = []

for nodo in grafo.elements:
    cantidad_aristas = len(nodo['aristas'])  # Contar aristas salientes
    if cantidad_aristas > max_aristas:
            max_aristas = cantidad_aristas
            nodos_maximos = [nodo['value']]  # Reiniciar la lista con el nuevo nodo máximo
    elif cantidad_aristas == max_aristas:
            nodos_maximos.append(nodo['value'])

print(nodos_maximos)


lista_n_y_a = []
for nodo in grafo.elements:
    valor_nodo = nodo['value']
    for arista in nodo['aristas']:
        lista_n_y_a.append((valor_nodo, arista['value']))

print(lista_n_y_a)

nodo_max_cant_a_llegan = []

# Iterar sobre cada tupla en la lista
for tupla in lista_n_y_a:
    aristas_salientes = tupla[1]  # Acceder al segundo valor de la tupla
    nodo_max_cant_a_llegan.append(aristas_salientes)

# print(nodo_max_cant_a_llegan)

counter = Counter(nodo_max_cant_a_llegan)

print("valor del nodo y las aristas que llegan a él: ",counter.most_common())

# print("nodos a los que llegan mayor cantidad de aristas:")

# for nodo,arista in enumerate(nodo_max_cant_a_llegan):
#      print("nodo:",nodo,"aristas: ",arista)