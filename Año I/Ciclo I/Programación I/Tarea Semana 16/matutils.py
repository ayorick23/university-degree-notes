def es_primo(n: int) -> bool:
    if n <= 1: #el número 1 no es primo
        return False
    
    for i in range(2, int(n**0.5) + 1): #iteración desde 2 hasta la raíz cuadrada de n
        if n % i == 0: #si n es divisible por i, no es primo
            return False
        
    return True

def factorial(n: int) -> int:
    if n < 0:
        print("El factorial no está definido para números negativos")
        return None
        
    if n == 0 or n == 1: #el factorial de 0 y 1 es 1
        return 1
    
    resultado = 1
    for i in range(2, n + 1): #iteración desde 2 hasta n
        resultado *= i #multiplicación acumulativa
        
    return resultado

def fibonacci(n: int) -> int:
    if n < 0:
        print("La serie de Fibonacci no está definida para números negativos")
        return None
    
    if n == 0: #el primer número de la serie es 0
        return 0
    elif n == 1: #el segundo número de la serie es 1
        return 1

    a = 0
    b = 1
    serie = [a, b]
    
    for i in range(2, n): #iteración desde 2 hasta n
        a, b = b, a + b #actualización de los valores de a y b
        serie.append(b) #agregar el nuevo número a la serie
        
    return serie