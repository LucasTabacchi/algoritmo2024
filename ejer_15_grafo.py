from grafo import Graph
from collections import Counter

grafo_maravillas = Graph(dirigido=False)

# Maravillas arquitectónicas
grafo_maravillas.insert_vertice("Gran Muralla China", other_value={"país": ["China"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Petra", other_value={"país": ["Jordania"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Coliseo de Roma", other_value={"país": ["Italia"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Chichén Itzá", other_value={"país": ["México"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Machu Picchu", other_value={"país": ["Perú"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Taj Mahal", other_value={"país": ["India"], "tipo": "arquitectónica"})
grafo_maravillas.insert_vertice("Cristo Redentor", other_value={"país": ["Brasil"], "tipo": "arquitectónica"})

# Maravillas naturales
grafo_maravillas.insert_vertice("Amazonas", other_value={"país": ["Brasil", "Perú", "Colombia"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Bahía de Ha Long", other_value={"país": ["Vietnam"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Cataratas del Iguazú", other_value={"país": ["Argentina", "Brasil"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Jeju", other_value={"país": ["Corea del Sur"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Komodo", other_value={"país": ["Indonesia"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Montaña de la Mesa", other_value={"país": ["Sudáfrica"], "tipo": "natural"})
grafo_maravillas.insert_vertice("Río subterráneo de Puerto Princesa", other_value={"país": ["Filipinas"], "tipo": "natural"})


grafo_maravillas.insert_arista("Gran Muralla China", "Petra", 5000)
grafo_maravillas.insert_arista("Gran Muralla China", "Coliseo de Roma", 8000)
grafo_maravillas.insert_arista("Gran Muralla China", "Chichén Itzá", 12000)
grafo_maravillas.insert_arista("Gran Muralla China", "Machu Picchu", 17000)
grafo_maravillas.insert_arista("Gran Muralla China", "Taj Mahal", 3500)
grafo_maravillas.insert_arista("Gran Muralla China", "Cristo Redentor", 17000)
grafo_maravillas.insert_arista("Petra", "Gran Muralla China", 5000)
grafo_maravillas.insert_arista("Petra", "Coliseo de Roma", 2300)
grafo_maravillas.insert_arista("Petra", "Chichén Itzá", 12000)
grafo_maravillas.insert_arista("Petra", "Machu Picchu", 15000)
grafo_maravillas.insert_arista("Petra", "Taj Mahal", 4000)
grafo_maravillas.insert_arista("Petra", "Cristo Redentor", 12000)
grafo_maravillas.insert_arista("Coliseo de Roma", "Gran Muralla China", 8000)
grafo_maravillas.insert_arista("Coliseo de Roma", "Petra", 2300)
grafo_maravillas.insert_arista("Coliseo de Roma", "Chichén Itzá", 10000)
grafo_maravillas.insert_arista("Coliseo de Roma", "Machu Picchu", 12000)
grafo_maravillas.insert_arista("Coliseo de Roma", "Taj Mahal", 7000)
grafo_maravillas.insert_arista("Coliseo de Roma", "Cristo Redentor", 9500)
grafo_maravillas.insert_arista("Chichén Itzá", "Gran Muralla China", 12000)
grafo_maravillas.insert_arista("Chichén Itzá", "Petra", 12000)
grafo_maravillas.insert_arista("Chichén Itzá", "Coliseo de Roma", 10000)
grafo_maravillas.insert_arista("Chichén Itzá", "Machu Picchu", 4200)
grafo_maravillas.insert_arista("Chichén Itzá", "Taj Mahal", 15000)
grafo_maravillas.insert_arista("Chichén Itzá", "Cristo Redentor", 7000)
grafo_maravillas.insert_arista("Machu Picchu", "Gran Muralla China", 17000)
grafo_maravillas.insert_arista("Machu Picchu", "Petra", 15000)
grafo_maravillas.insert_arista("Machu Picchu", "Coliseo de Roma", 12000)
grafo_maravillas.insert_arista("Machu Picchu", "Chichén Itzá", 4200)
grafo_maravillas.insert_arista("Machu Picchu", "Taj Mahal", 15000)
grafo_maravillas.insert_arista("Machu Picchu", "Cristo Redentor", 3500)
grafo_maravillas.insert_arista("Taj Mahal", "Gran Muralla China", 3500)
grafo_maravillas.insert_arista("Taj Mahal", "Petra", 4000)
grafo_maravillas.insert_arista("Taj Mahal", "Coliseo de Roma", 7000)
grafo_maravillas.insert_arista("Taj Mahal", "Chichén Itzá", 15000)
grafo_maravillas.insert_arista("Taj Mahal", "Machu Picchu", 15000)
grafo_maravillas.insert_arista("Taj Mahal", "Cristo Redentor", 14000)
grafo_maravillas.insert_arista("Cristo Redentor", "Gran Muralla China", 17000)
grafo_maravillas.insert_arista("Cristo Redentor", "Petra", 12000)
grafo_maravillas.insert_arista("Cristo Redentor", "Coliseo de Roma", 9500)
grafo_maravillas.insert_arista("Cristo Redentor", "Chichén Itzá", 7000)
grafo_maravillas.insert_arista("Cristo Redentor", "Machu Picchu", 3500)
grafo_maravillas.insert_arista("Cristo Redentor", "Taj Mahal", 14000)

grafo_maravillas.insert_arista("Amazonas", "Bahía de Ha Long", 15000)
grafo_maravillas.insert_arista("Amazonas", "Cataratas del Iguazú", 3000)
grafo_maravillas.insert_arista("Amazonas", "Jeju", 16000)
grafo_maravillas.insert_arista("Amazonas", "Komodo", 18000)
grafo_maravillas.insert_arista("Amazonas", "Montaña de la Mesa", 13000)
grafo_maravillas.insert_arista("Amazonas", "Río subterráneo de Puerto Princesa", 19000)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Amazonas", 15000)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Cataratas del Iguazú", 18000)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Jeju", 3000)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Komodo", 2500)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Montaña de la Mesa", 11000)
grafo_maravillas.insert_arista("Bahía de Ha Long", "Río subterráneo de Puerto Princesa", 1600)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Amazonas", 3000)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Bahía de Ha Long", 18000)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Jeju", 17000)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Komodo", 16000)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Montaña de la Mesa", 8000)
grafo_maravillas.insert_arista("Cataratas del Iguazú", "Río subterráneo de Puerto Princesa", 17000)
grafo_maravillas.insert_arista("Jeju", "Amazonas", 16000)
grafo_maravillas.insert_arista("Jeju", "Bahía de Ha Long", 3000)
grafo_maravillas.insert_arista("Jeju", "Cataratas del Iguazú", 17000)
grafo_maravillas.insert_arista("Jeju", "Komodo", 3500)
grafo_maravillas.insert_arista("Jeju", "Montaña de la Mesa", 12000)
grafo_maravillas.insert_arista("Jeju", "Río subterráneo de Puerto Princesa", 1500)
grafo_maravillas.insert_arista("Komodo", "Amazonas", 18000)
grafo_maravillas.insert_arista("Komodo", "Bahía de Ha Long", 2500)
grafo_maravillas.insert_arista("Komodo", "Cataratas del Iguazú", 16000)
grafo_maravillas.insert_arista("Komodo", "Jeju", 3500)
grafo_maravillas.insert_arista("Komodo", "Montaña de la Mesa", 11000)
grafo_maravillas.insert_arista("Komodo", "Río subterráneo de Puerto Princesa", 2500)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Amazonas", 13000)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Bahía de Ha Long", 11000)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Cataratas del Iguazú", 8000)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Jeju", 12000)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Komodo", 11000)
grafo_maravillas.insert_arista("Montaña de la Mesa", "Río subterráneo de Puerto Princesa", 14000)

arbol_expansion_minima_arquitectonicas = grafo_maravillas.kruskal('Cristo Redentor')
print(arbol_expansion_minima_arquitectonicas)

print()

for arista in arbol_expansion_minima_arquitectonicas[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()

arbol_expansion_minima_naturales = grafo_maravillas.kruskal('Cataratas del Iguazú')
print(arbol_expansion_minima_naturales)

print()

for arista in arbol_expansion_minima_naturales[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()

paises_arquitectonicas = set()
paises_naturales = set()
    
    # Recorremos todos los nodos del grafo y clasificamos los países por tipo de maravilla
for nodo in grafo_maravillas.elements:
        tipo = nodo['other_value']['tipo']
        paises = nodo['other_value']['país']
        
        if tipo == 'arquitectónica':
            for pais in paises:
                paises_arquitectonicas.add(pais)  # Añadir cada país individualmente
        elif tipo == 'natural':
            for pais in paises:
                paises_naturales.add(pais)
    
    # Encontramos los países que tienen ambos tipos de maravillas
paises_ambos_tipos = paises_arquitectonicas.intersection(paises_naturales)

print(f"los paises con maravillas arquitectónicas y naturales son {paises_ambos_tipos}")

print()

paises_mas_de_una_maraviila_a = []
paises_mas_de_una_maraviila_n = []
for nodo in grafo_maravillas.elements:
        tipo = nodo['other_value']['tipo']
        paises = nodo['other_value']['país']

        if tipo == 'arquitectónica':
            for pais in paises:
                paises_mas_de_una_maraviila_a.append((pais,))
        elif tipo == 'natural':
            for pais in paises:
                paises_mas_de_una_maraviila_n.append((pais,))

# print(paises_mas_de_una_maraviila_a)
# print(paises_mas_de_una_maraviila_n)
print()
counter_arquitectonicas = Counter(paises_mas_de_una_maraviila_a)
paises_con_mas_de_una_maravilla = [pais for pais, count in counter_arquitectonicas.items() if count > 1]

if paises_con_mas_de_una_maravilla:
    print("Países con más de una maravilla arquitectónica:", paises_con_mas_de_una_maravilla)
else:
    print("No hay países con más de una maravilla arquitectónica.")

# print(counter_arquitectonicas)
# print(counter_arquitectonicas.most_common())

counter_naturales = Counter(paises_mas_de_una_maraviila_n)
paises_con_mas_de_una_maravilla = [pais for pais, count in counter_naturales.items() if count > 1] #itera sobre cada par clave-valor en el Counter

if paises_con_mas_de_una_maravilla:
    print("Países con más de una maravilla natural:", paises_con_mas_de_una_maravilla)
else:
    print("No hay países con más de una maravilla natural.")