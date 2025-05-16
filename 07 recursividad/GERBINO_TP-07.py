#  ejercicio 1

def factorial(n):
    if n == 0: # establecemos un caso base
        return 1 # paramos la ejecucion retornando uno
    else: # si no
        return n * factorial(n - 1) # iniciamos recursividad
    
print(factorial(5))
    
# ejercicio 2

def fibonacci(n):
    if n == 0: # establecemos el caso base
        return 0 # si es cero paramos y lo retornamos
    elif n == 1: # establecemos otra condicion para el caso base
        return 1 # si es uno paramos y lo retornamos
    else: # si no
        return fibonacci(n - 1) + fibonacci(n - 2) # iniciamos recursividad
    
print(fibonacci(6))
    
# ejercicio 3

def potencia(b, e):
    if e == 0: # establecemos el caso base
        return 1 # si es cero paramos y lo retornamos
    else: # si no
        return b * potencia(b, e - 1) # iniciamos recursividad
    
print(potencia(6, 3))
    
# ejercicio 4

def decimalABinario(n):
    if n == 0: # establecemos el caso base
        return "" # si es cero paramos y retornamos
    else: # si no
        return decimalABinario(n // 2) + str(n % 2) # pasamos a binario y concatenamos
    
print(decimalABinario(6327))
    
# ejercicio 5
    
def chequearPalindromo(palabra, inicio=0):
    final = len(palabra) - 1 - inicio # creamos indice final
    if inicio >= final: # establecemos el caso base si se cruzan
        return True # si terminamos la palabra retornamos true
    if palabra[inicio] != palabra[final]: # si ultima letra no es igual a primera
      return False # no es palindromo
    return chequearPalindromo(palabra, inicio + 1) # pasamos a la siguiente
    
print(chequearPalindromo("oso"))
print(chequearPalindromo("vector"))
    
# ejercicio 6

def sumaDigitos(n):
    if n < 10: # establecemos el caso base
        return n # retornamos el numero
    else: # si no
        return n % 10 + sumaDigitos(n // 10) # sumamos
    
print(sumaDigitos(15))
    
# ejercicio 7

def contarBloques(n):
    if n == 1: # establecemos el caso base
        return 1 # devolvemos uno
    else: # si no
        return n + contarBloques(n - 1) # sumamos
    
print(contarBloques(32))
    
# ejercicio 8

def contarDigito(numero, digito):
    if numero == 0: # establecemos el caso base
        return 0 # retornamos cero si el numero es cero
    else: # si no
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contarDigito(numero // 10, digito)
        else:
            return contarDigito(numero // 10, digito)
        
print(contarDigito(23413,4))