from cola import Queue
from pila import Stack
from pila import Stack
from random import randint

# Ejercicio_1
# cola_char = Queue()

# for i in range(10):
#     letra = chr(randint(65, 90))
#     cola_char.arrive(letra)

# for i in range(cola_char.size()):
#     print(cola_char.on_front())
#     cola_char.move_to_end()

# print()
# vocales = ['A', 'E', 'I', 'O', 'U']

# for i in range(cola_char.size()):
#     if cola_char.on_front() in vocales:
#         cola_char.attention()
#     else:
#         cola_char.move_to_end()

# for i in range(cola_char.size()):
#     print(cola_char.on_front())
#     cola_char.move_to_end()

# Ejercicio_2
# cola = Queue()
# pila = Stack()

# for i in range(5):
#     cola.arrive(randint(1,10))

# for i in range(cola.size()):
#     print(cola.on_front())
#     cola.move_to_end()

# print()

# while cola.size() > 0:
#     valor = cola.attention()
#     pila.push(valor)

# while pila.size() > 0:
#     # print(pila.on_top())
#     valor = pila.pop()
#     cola.arrive(valor)

# for i in range(cola.size()):
#     print(cola.on_front())
#     cola.move_to_end()

# Ejercicio_3

pila = Stack()
cola = Queue()

palabra = input('ingrese una palabra ')

for letra in palabra:
    pila.push(letra)
    cola.arrive(letra)

while pila.size()>0:
    print(pila.pop())

print("-")

while cola.size()>0:
    print(cola.attention(), end = " ")


# while cola.size() > 0 and cola.on_front() == pila.on_top():
#     pila.pop()
#     cola.attention()

# if cola.size() > 0:
#     print('no es palindromo')
# else:
#     print('es palindromo')




