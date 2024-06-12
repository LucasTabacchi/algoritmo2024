from pila import Stack
from random import randint

#! ejercicio 1 
# pila = Stack()
# Pila_aux = Stack()
# cont = 0

# numero = int(input("ingrese un numero: "))

# for i in range(10):
#          pila.push(randint(1, 10))

# while pila.size()>0:
#         data = pila.pop()
#         print(data)
#         if data == numero:
#              Pila_aux.push(data)
#              cont += 1 


# print('la cantidad de veces que aparece el numero es:',cont)

# while pila.size() > 0 :
#     valores = pila.pop()
#     if valores == numero:
#         Pila_aux.push(valores)
#         cont += 1 

# while Pila_aux.size() > 0:
#     data = Pila_aux.pop()
#     pila.push(data)


#!ejercicio 2
# pila = Stack()
# pila_aux= Stack()


# for i in range(5):
#           pila.push(randint(1, 10))

# while pila.size() > 0:
#         valor = pila.pop()
#         print(valor)
#         pila_aux.push(valor)

# print()    

# numero = int(input('ingrese el numero que reemplazara de pila: '))
# numero_nuevo = int(input('ingrese el numero nuevo por el que se va reemplazar: '))

# while pila_aux.size() > 0:
#         valor = pila_aux.pop()
#         if valor == numero :
#                 valor = numero_nuevo
#                 pila.push(valor)
#         else:
#             pila.push(valor)

# while pila.size() > 0:
#         print(pila.pop())


#! ejercicio 4
# pila = Stack()
# pila_aux = Stack()

# for i in range(5):
#     pila.push(randint(1,10))

# while pila.size() > 0:
#     valor = pila.pop()
#     print(valor)
#     pila_aux.push(valor)

# print()

# while pila_aux.size() > 0:
#     valor = pila_aux.pop()
#     print(valor)

#! ejercicio 5 #este es el que hice yo
# pila = Stack()
# pila_aux = Stack()

# palabra = input ('ingrese la palabra: ')
# palabra_2 = palabra

# for i in palabra:
#     pila.push(i)


# for j in reversed(palabra_2):
#      pila_aux.push(j)


# while pila.size() > 0 and pila.on_top() == pila_aux.on_top():
#             pila.pop()
#             pila_aux.pop()

# if pila.size() == 0 :
#      print('la palabra es palindromo')
# else:
#      print('la palabra no es palindromo')




# pila1 = Stack()
# pila2 = Stack()
# pila3 = Stack()


# # palabra = input('ingrese un palabra ')
# # for letra in palabra:
# #      pila1.push(letra)

# # while pila1.size() > 0:
# #      valor = pila1.pop()
# #      pila2.push(valor)
# #      pila3.push(valor)

# # while pila3.size() > 0:
# #      pila1.push(pila3.pop())

# # while pila1.size() > 0 and pila1.on_top() == pila2.on_top():
# #      pila1.pop()
# #      pila2.pop()

# # if pila1.size() == 0:
# #      print('es palindromo')
# # else:
# #      print('no es palindromo')

# # if pila1 == pila2:
# #     print('es palindromo')
# # else:
# #     print('no es palindromo')


# Ejer_16 
# pila = Stack()
# pila_2 = Stack()
# pila_aux = Stack()

# lista_per_epi_5 = [["Luke Skywalker"], ["Princess Leia"], ["Han Solo"], ["Chewbacca"], ["Darth Vader"], ["Yoda"], ["Lando Calrissian"], ["C-3PO"], ["R2-D2"], ["Emperor Palpatine"], ["Boba Fett"]]

# lista_per_epi_7 = [["Rey"], ["Finn"], ["Kylo Ren"], ["Han Solo"], ["Princess Leia"], ["Poe Dameron"], ["BB-8"], ["Chewbacca"], ["Luke Skywalker"], ["Supreme Leader Snoke"], ["Maz Kanata"]]

# for p in lista_per_epi_5:
#     pila.push(p)

# for p in lista_per_epi_7:
#     pila_2.push(p)

# while pila.size() > 0:
#     valor = pila.pop()
#     print(valor)

# print()
    
# while pila_2.size() > 0:
#     valor = pila_2.pop()
#     print(valor)

# while pila.size() > 0 and pila_2.size() > 0:
#     p = pila.pop()
#     # print(p)
#     p_2 = pila_2.pop()
#     # print(p_2)
#     if p == p_2:
#         pila_aux.push(p)
#     else:
#         pila.pop()
#         pila_2.pop()


# while pila.size() > 0 and pila_2.size() > 0:
#     nombre1 = pila.pop()
#     nombre2 = pila_2.pop()

#     if nombre1 == nombre2:
#         # Si los nombres son iguales, agrégalos a la pila de duplicados
#         pila_aux.push(nombre1)
#     else:
#         # Si los nombres son diferentes, agrega los nombres únicos al conjunto
#         nombres_unicos.append(nombre1)
#         nombres_unicos.append(nombre2)

# print('nombres duplicados')

# while pila_aux.size() > 0:
#     print(pila_aux.pop())

# while pila_aux.size() > 0:
#     print(pila_aux.pop())


    





        


 



    



