from grafo import Graph
from heap import HeapMin

lista_ambientes = ["cocina", "comedor", "cochera", "quincho",
"baño 1", "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

grafo_ambientes = Graph(dirigido=False)

for ambiente in lista_ambientes:
    grafo_ambientes.insert_vertice(ambiente)

grafo_ambientes.insert_arista("cocina", "comedor", 3)
grafo_ambientes.insert_arista("cocina", "patio", 4)
grafo_ambientes.insert_arista("cocina", "sala de estar", 5)
grafo_ambientes.insert_arista("comedor", "sala de estar", 4)
grafo_ambientes.insert_arista("comedor", "patio", 5)
grafo_ambientes.insert_arista("comedor", "terraza", 7)
grafo_ambientes.insert_arista("cochera", "patio", 8)
grafo_ambientes.insert_arista("cochera", "quincho", 6)
grafo_ambientes.insert_arista("cochera", "sala de estar", 9)
grafo_ambientes.insert_arista("quincho", "patio", 4)
grafo_ambientes.insert_arista("quincho", "terraza", 7)
grafo_ambientes.insert_arista("quincho", "cochera", 6)
grafo_ambientes.insert_arista("baño 1", "sala de estar", 3)
grafo_ambientes.insert_arista("baño 1", "habitación 1", 2)
grafo_ambientes.insert_arista("baño 1", "patio", 6)
grafo_ambientes.insert_arista("baño 2", "habitación 2", 2)
grafo_ambientes.insert_arista("baño 2", "sala de estar", 4)
grafo_ambientes.insert_arista("baño 2", "patio", 7)
grafo_ambientes.insert_arista("habitación 1", "sala de estar", 4)
grafo_ambientes.insert_arista("habitación 1", "baño 1", 2)
grafo_ambientes.insert_arista("habitación 1", "terraza", 8)
grafo_ambientes.insert_arista("habitación 2", "sala de estar", 4)
grafo_ambientes.insert_arista("habitación 2", "baño 2", 2)
grafo_ambientes.insert_arista("habitación 2", "terraza", 8)
grafo_ambientes.insert_arista("sala de estar", "terraza", 6)
grafo_ambientes.insert_arista("sala de estar", "patio", 5)
grafo_ambientes.insert_arista("sala de estar", "cocina", 5)
grafo_ambientes.insert_arista("sala de estar", "habitación 1", 4)
grafo_ambientes.insert_arista("sala de estar", "habitación 2", 4)
grafo_ambientes.insert_arista("terraza", "patio", 5)
grafo_ambientes.insert_arista("terraza", "sala de estar", 6)
grafo_ambientes.insert_arista("terraza", "quincho", 7)
grafo_ambientes.insert_arista("patio", "cocina", 4)
grafo_ambientes.insert_arista("patio", "quincho", 4)
grafo_ambientes.insert_arista("patio", "terraza", 5)
grafo_ambientes.insert_arista("patio", "sala de estar", 5)
grafo_ambientes.insert_arista("patio", "cochera", 8)

grafo_ambientes.show_graph()

arbol_expansion = grafo_ambientes.kruskal('cocina')
print(arbol_expansion)


for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()

camino = grafo_ambientes.dijkstra('habitación 1')
destino = 'sala de estar'
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0])
        destino = value[1][2]
camino_completo.reverse()
print(f'el camino mas corto es: {'-'.join(camino_completo)} con un costo de {peso_total}')

