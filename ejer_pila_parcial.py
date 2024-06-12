from pila import Stack

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500 ,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500 ,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700 ,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000 ,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000 ,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

pila_dino = Stack()
pila_aux = Stack()
pilas_letras = Stack()

for dino in dinosaurios:
    pila_dino.push(dino)

# while pila_dino.size() > 0 :
#     print(pila_dino.pop())

especies = set()

while pila_dino.size() > 0:
    dino = pila_dino.pop()
    especies.add(dino['especie'])
    pila_aux.push(dino)

numero_especies = len(especies)
print(f"Número de especies: {numero_especies}")

while pila_aux.size() > 0:
    pila_dino.push(pila_aux.pop())

print("-")

# while pila_dino.size() > 0 :
#     print(pila_dino.pop())

descubridores = set()
while pila_dino.size() > 0:
    dino = pila_dino.pop()
    descubridores.add(dino['descubridor'])
    pila_aux.push(dino)

numero_descubridores = len(descubridores)
print(f"Número de descubridores únicos: {numero_descubridores}")

while pila_aux.size() > 0:
    pila_dino.push(pila_aux.pop())


# while pila_dino.size() > 0 :
#     print(pila_dino.pop())

print("-")

print("dinosaurios que empiezan con T: ")
while pila_dino.size() > 0:
    dino = pila_dino.pop()
    if dino['nombre'].startswith("T"):
        print(dino)
    pila_aux.push(dino)

while pila_aux.size() > 0:
    pila_dino.push(pila_aux.pop())

# while pila_dino.size() > 0 :
#     print(pila_dino.pop())

print("-")

print("Dinosaurios que pesan menos de 275 kg:")
while pila_dino.size() > 0:
    dino = pila_dino.pop()
    peso = dino['peso']
    if peso < 275:
        print(dino)
    pila_aux.push(dino)

while pila_aux.size() > 0:
    pila_dino.push(pila_aux.pop())


# while pila_dino.size() > 0 :
#     print(pila_dino.pop())

print("-")

print("dinosaurios que empiezan con A, Q o S: ")
while pila_dino.size() > 0:
    dino = pila_dino.pop()
    if dino['nombre'].startswith(('A','Q','S')):
        pilas_letras.push(dino)
    else:
        pila_aux.push(dino)

while pilas_letras.size() > 0:
    print(pilas_letras.pop())