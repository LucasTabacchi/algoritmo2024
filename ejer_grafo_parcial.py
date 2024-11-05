from grafo import Graph

grafo_personajes = Graph(dirigido=False)

lista_personajes= ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C 3PO", "Leia", "Rey", "Kylo Ren",
                    "Chewbacca", "Han Solo", "R2 D2", "BB 8"]

for personaje in lista_personajes:
    grafo_personajes.insert_vertice(personaje)


grafo_personajes.insert_arista("Luke Skywalker", "Han Solo", 3)  
grafo_personajes.insert_arista("Luke Skywalker", "Leia", 2)
grafo_personajes.insert_arista("Han Solo", "Leia", 4)
grafo_personajes.insert_arista("Darth Vader", "Luke Skywalker", 6) 
grafo_personajes.insert_arista("Leia", "C 3PO", 3)
grafo_personajes.insert_arista("Leia", "Chewbacca", 3)
grafo_personajes.insert_arista("C 3PO", "R2 D2", 9)
grafo_personajes.insert_arista("Chewbacca", "Han Solo", 3)
grafo_personajes.insert_arista("Yoda", "Luke Skywalker", 1)
grafo_personajes.insert_arista("Yoda", "Darth Vader", 2)
grafo_personajes.insert_arista("Boba Fett", "Han Solo", 8)
grafo_personajes.insert_arista("BB 8", "Rey", 10)
grafo_personajes.insert_arista("Kylo Ren", "Rey", 3)
grafo_personajes.insert_arista("Kylo Ren", "Leia", 2)

grafo_personajes.show_graph()
print()
aem = grafo_personajes.kruskal('Luke Skywalker')
print(aem)

for aristas in aem:
    if '-' in aristas:
        for arista in aristas.split(';'):
            origen, destino, peso = arista.split('-')
            print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()

yoda = False
for arista in aem[0].split(';'):
        origen, destino, peso = arista.split('-')
        if origen == "Yoda" or destino == "Yoda":
            yoda = True
            break

if yoda:
    print("Yoda está presente en el Árbol de Expansión Mínimo.")
else:
    print("Yoda NO está presente en el Árbol de Expansión Mínimo.")

print()

max_peso = 0
personajes_max = ()

for nodo in grafo_personajes.elements:
    for arista in nodo['aristas']:
        if arista['peso'] > max_peso:
            max_peso = arista['peso'] 
            personajes_max = (nodo['value'], arista['value'])

print(f"Los personajes que comparten el mayor número de episodios ({max_peso} episodios) son: {personajes_max[0]} y {personajes_max[1]}")
