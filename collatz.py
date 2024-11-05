# def collatz_sequence(n):
#     if n <= 0 or not isinstance(n, int):
#         return "Error: Por favor, ingrese un número entero positivo."
    
#     sequence = []
    
#     while n != 1:
#         sequence.append(n)
#         if n % 2 == 0:
#             n //= 2  # Si es par, dividir entre 2
#         else:
#             n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1

#     sequence.append(1)  # Agregar el 1 al final de la secuencia
#     return sequence

# def main():
#     while True:
#         try:
#             user_input = int(input("Ingrese un número entero positivo (-1 para salir): "))
#             if user_input == -1:
#                 print("Saliendo del programa.")
#                 break
#             print("Secuencia de Collatz:", collatz_sequence(user_input))
#         except ValueError:
#             print("Error: Por favor, ingrese un número entero positivo.")

# if __name__ == "__main__":
#     main()

# def collatz_iterations(n):
    
#     if not isinstance(n, int) or n <= 0:
#         raise ValueError("Por favor, ingrese un número entero positivo.")

#     sequence = []
#     iterations = 0

#     while n != 1:
#         sequence.append(n)
#         if n % 2 == 0:
#             n //= 2  # Si es par, dividir entre 2
#         else:
#             n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
#         iterations += 1

#     # Agregar los números finales de la secuencia
#     sequence.extend([4, 2, 1])

#     return iterations, sequence

# # Ejemplo de uso
# try:
#     number = int(input("Ingrese un número entero positivo: "))
#     iter_count, result_sequence = collatz_iterations(number)
#     print(f"Número de iteraciones: {iter_count}")
#     print(f"Números intermedios: {result_sequence}")
# except ValueError as e:
#     print(e)

# def collatz_iterations(n):

#     if not isinstance(n, int) or n <= 0:
#         raise ValueError("Por favor, ingrese un número entero positivo.")

#     sequence = []
#     iterations = 0

#     while n != 1:
#         sequence.append(n)
#         if n % 2 == 0:
#             n //= 2  # Si es par, dividir entre 2
#         else:
#             n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
#         iterations += 1

#     # Agregar los números finales de la secuencia
#     sequence.extend([4, 2, 1])

#     return iterations, sequence

# # Casos de prueba
# def run_tests():
#     test_cases = [
#         (1, 0, [4, 2, 1]),          # Caso de prueba 1
#         (2, 1, [2, 1]),             # Caso de prueba 2
#         (3, 7, [3, 10, 5, 16, 8, 4, 2, 1]),  # Caso de prueba 3
#         (4, 2, [4, 2, 1]),          # Caso de prueba 4
#         (5, 5, [5, 16, 8, 4, 2, 1]), # Caso de prueba 5
#         (6, 8, [6, 3, 10, 5, 16, 8, 4, 2, 1]),  # Caso de prueba 6
#         (7, 16, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]), # Caso de prueba 7
#         (8, 3, [8, 4, 2, 1]),        # Caso de prueba 8
#         (9, 19, [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]), # Caso de prueba 9
#         (10, 6, [10, 5, 16, 8, 4, 2, 1]), # Caso de prueba 10
#         (15, 17, [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]), # Caso de prueba 11
#         (100, 25, [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]) # Caso de prueba 12
#     ]

#     for i, (input_value, expected_iterations, expected_sequence) in enumerate(test_cases):
#         try:
#             iterations, sequence = collatz_iterations(input_value)
#             assert iterations == expected_iterations, f"Error en caso {i + 1}: se esperaban {expected_iterations} iteraciones, se obtuvieron {iterations}."
#             assert sequence == expected_sequence, f"Error en caso {i + 1}: se esperaban {expected_sequence}, se obtuvieron {sequence}."
#             print(f"Caso {i + 1} exitoso: Entrada {input_value}, Iteraciones: {iterations}, Secuencia: {sequence}")
#         except ValueError as e:
#             print(f"Error en caso {i + 1} con entrada {input_value}: {e}")

# # Ejecutar los casos de prueba
# run_tests()

# def collatz_iterations(n):
    
#     if not isinstance(n, int) or n <= 0:
#         raise ValueError("Por favor, ingrese un número entero positivo.")

#     sequence = []
#     iterations = 0

#     while n != 1:
#         sequence.append(n)
#         if n % 2 == 0:
#             n //= 2  # Si es par, dividir entre 2
#         else:
#             n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
#         iterations += 1

#     # Agregar los números finales de la secuencia
#     sequence.extend([4, 2, 1])

#     return iterations, sequence

# def main():
#     """
#     Función principal que solicita al usuario un número,
#     ejecuta el algoritmo de Collatz y muestra los resultados.
#     """
#     try:
#         # Solicitar al usuario que ingrese un número entero positivo
#         number = int(input("Ingrese un número entero positivo para iniciar la secuencia de Collatz: "))
        
#         # Invocar la función collatz_iterations con el número ingresado
#         iter_count, result_sequence = collatz_iterations(number)
        
#         # Mostrar el número de iteraciones y la secuencia
#         print(f"Número de iteraciones: {iter_count}")
#         print(f"Números intermedios hasta alcanzar la secuencia 4, 2, 1: {result_sequence}")
    
#     except ValueError as e:
#         # Capturar y mostrar errores de entrada
#         print(e)

# # Ejecutar la función principal
# if __name__ == "__main__":
#     main()

# import math

# def collatz_iterations(n):
#     """
#     Esta función implementa el algoritmo de Collatz.
    
#     Parámetros:
#     n (int): Un número entero positivo.

#     Retorna:
#     tuple: Una tupla que contiene el número de iteraciones y la lista de números intermedios.
    
#     Excepciones:
#     ValueError: Si n no es un número entero positivo.
#     """
    
#     if not isinstance(n, int) or n <= 0:
#         raise ValueError("Por favor, ingrese un número entero positivo.")

#     sequence = []
#     iterations = 0

#     # Verificar si n es potencia de 2
#     if (n & (n - 1)) == 0:  # Verifica si n es potencia de 2
#         iterations = int(math.log2(n))  # Número de iteraciones
#         sequence = [n // (2 ** i) for i in range(iterations)] + [1]
#     else:
#         while n != 1:
#             sequence.append(n)
#             if n % 2 == 0:
#                 n //= 2  # Si es par, dividir entre 2
#             else:
#                 n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
#             iterations += 1

#         # Agregar los números finales de la secuencia
#         sequence.extend([4, 2, 1])

#     return iterations, sequence

# def main():
#     """
#     Función principal que solicita al usuario un número,
#     ejecuta el algoritmo de Collatz y muestra los resultados.
#     """
#     try:
#         # Solicitar al usuario que ingrese un número entero positivo
#         number = int(input("Ingrese un número entero positivo para iniciar la secuencia de Collatz: "))
        
#         # Invocar la función collatz_iterations con el número ingresado
#         iter_count, result_sequence = collatz_iterations(number)
        
#         # Mostrar el número de iteraciones y la secuencia
#         print(f"Número de iteraciones: {iter_count}")
#         print(f"Números intermedios hasta alcanzar la secuencia 4, 2, 1: {result_sequence}")
    
#     except ValueError as e:
#         # Capturar y mostrar errores de entrada
#         print(e)

# # Ejecutar la función principal
# if __name__ == "__main__":
#     main()

# import sys
# import math

# def collatz_iterations(n):
#     """
#     Esta función implementa el algoritmo de Collatz.
    
#     Parámetros:
#     n (int): Un número entero positivo.

#     Retorna:
#     tuple: Una tupla que contiene el número de iteraciones y la lista de números intermedios.
    
#     Excepciones:
#     ValueError: Si n no es un número entero positivo.
#     """
    
#     if not isinstance(n, int) or n <= 0:
#         raise ValueError("Por favor, ingrese un número entero positivo.")

#     sequence = []
#     iterations = 0

#     # Verificar si n es potencia de 2
#     if (n & (n - 1)) == 0:  # Verifica si n es potencia de 2
#         iterations = int(math.log2(n))  # Número de iteraciones
#         sequence = [n // (2 ** i) for i in range(iterations)] + [1]
#     else:
#         while n != 1:
#             sequence.append(n)
#             if n % 2 == 0:
#                 n //= 2  # Si es par, dividir entre 2
#             else:
#                 n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
#             iterations += 1

#         # Agregar los números finales de la secuencia
#         sequence.extend([4, 2, 1])

#     return iterations, sequence

# def main():
#     """
#     Función principal que obtiene el número desde los argumentos
#     de la línea de comandos, ejecuta el algoritmo de Collatz 
#     y muestra los resultados.
#     """
#     try:
#         # Verificar si se proporcionó un argumento
#         if len(sys.argv) != 2:
#             print("Uso: python collatz.py <número entero positivo>")
#             return
        
#         # Obtener el número desde el argumento
#         number = int(sys.argv[1])
        
#         # Invocar la función collatz_iterations con el número ingresado
#         iter_count, result_sequence = collatz_iterations(number)
        
#         # Mostrar el número de iteraciones y la secuencia
#         print(f"Número de iteraciones: {iter_count}")
#         print(f"Números intermedios hasta alcanzar la secuencia 4, 2, 1: {result_sequence}")
    
#     except ValueError as e:
#         # Capturar y mostrar errores de entrada
#         print(e)

# # Ejecutar la función principal
# if __name__ == "__main__":
#     main()

import sys
import math

def collatz_iterations(n):
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Por favor, ingrese un número entero positivo.")

    sequence = []
    iterations = 0

    # Verificar si n es potencia de 2
    if (n & (n - 1)) == 0:  # Verifica si n es potencia de 2
        iterations = int(math.log2(n))  # Número de iteraciones
        sequence = [n // (2 ** i) for i in range(iterations)] + [1]
    else:
        while n != 1:
            sequence.append(n)
            if n % 2 == 0:
                n //= 2  # Si es par, dividir entre 2
            else:
                n = n * 3 + 1  # Si es impar, multiplicar por 3 y sumar 1
            iterations += 1

        # Agregar los números finales de la secuencia
        sequence.extend([4, 2, 1])

    return iterations, sequence

def main():
    """
    Función principal que obtiene el número desde los argumentos
    de la línea de comandos, ejecuta el algoritmo de Collatz 
    y muestra los resultados.
    """
    try:
        # Verificar si se proporcionó un argumento
        if len(sys.argv) != 2:
            print("Uso: python collatz.py <número entero positivo>")
            return
        
        # Obtener el número desde el argumento
        number = int(sys.argv[1])
        
        # Invocar la función collatz_iterations con el número ingresado
        iter_count, result_sequence = collatz_iterations(number)
        
        # Mostrar el número de iteraciones y la secuencia
        print(f"Número de iteraciones: {iter_count}")
        print(f"Números intermedios hasta alcanzar la secuencia 4, 2, 1: {result_sequence}")
    
    except ValueError as e:
        # Capturar y mostrar errores de entrada
        print(e)

# Ejecutar la función principal
if __name__ == "__main__":
    main()