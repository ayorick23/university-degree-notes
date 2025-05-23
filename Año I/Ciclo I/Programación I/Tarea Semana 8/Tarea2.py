"""
Escribe un programa en Python que solicite al usuario una lista de números enteros y los almacene en un array.
Luego, implementa un algoritmo de ordenamiento manual usando bucles (sin usar sort() ni sorted() u otro método 
que facilite el ordenamiento ya hecho en python ) para ordenar los números de menor a mayor.

Requisitos:
- Usa un bucle anidado para comparar y ordenar los elementos.
- No utilices métodos de ordenamiento como sort() ni sorted() u otro método.
- Muestra el array antes y después de la ordenación.
"""

#definicion de lista
numeros = []

#manejo de excepcion para que el usuario ingrese numeros enteros
while True:
    try:
        #solicitar numeros al usuario
        for i in range(5):
            num = int(input(f"Ingrese el numero entero en la posicion {i+1}: "))
            numeros.append(num)
        break #romper el bucle en caso que se llene la lista correctamente
    except ValueError:
        print("ERROR: Ingrese solo numeros enteros")

#imprimir lista desordenada
print(f"Lista de numeros desordenada: {numeros}")

#asignando una variable para longitud de la lista
n = len(numeros)

#algoritmo para ordenar la lista
for i in range(n):
    for j in range(0, n - i - 1): #evita que se vuelva a comparar innecesariamente
        if numeros[j] > numeros[j + 1]:
            #intercambia la posicion
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

#mostrar lista ordenada
print(f"Lista de numeros ordenada: {numeros}")