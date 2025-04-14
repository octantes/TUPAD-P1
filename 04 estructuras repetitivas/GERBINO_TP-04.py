# ejercicio 1

for i in range(0, 101):
        print(i)

# ejercicio 2

entero = int(input("ingresa un entero: ")) # pedimos el valor al usuario
digitos = len(str(entero)) # pasamos int a string y contamos
print (f"el entero {entero} tiene {digitos} dígitos.") # imprimimos resultado

# ejercicio 3

valorA = int(input("ingresa el valor de A: ")) # pedimos primer valor
valorB = int(input("ingresa el valor de B: ")) # pedimos segundo valor
suma = 0 # inicializamos en cero la suma
if valorA < valorB: #chequeamos si A es menor que B
  principio = valorA + 1 # si es menor, empezamos por A+1
  fin = valorB # terminamos en b
else:
     principio = valorB + 1 # si A es mayor, empezamos por B+1
     fin = valorA # terminamos en A
for i in range(principio, fin): # iteramos desde el principio hasta el fin
    suma += i # sumamos al acumulador
print(f"la suma de los numeros entre {principio} y {fin-1} es: {suma}")

# ejercicio 4

suma = 0 # inicializamos la suma
valor = int(input("ingresa un entero a sumar")) # pedimos entero al usuario
while valor != 0: # mientras el valor sea distinto de cero
    suma += valor # sumamos al acumulador
    valor = int(input("ingresa un entero a sumar")) # volvemos a pedir entero al usuario
print(f"la suma es: {suma}") # imprimimos resultado

# ejercicio 5

import random # importamos libreria random
adivinanza = random.randint(0, 9) # creamos num aleatorio entre 0 y 9
intentos = 0  # variable para contar los intentos
intento = 99 # inicializamos intento en un valor fuera del rango
while intento != adivinanza:  # loopeamos hasta que el usuario adivine
    intento = int(input("adivina el numero entre 0 y 9: ")) # pedimos al usuario que ingrese un número
    intentos += 1  # Incrementar el contador de intentos
    if intento == adivinanza: # comparamos intento con adivinanza
        print("adivinaste")
    elif intento < adivinanza:
        print("tu intento es menor que el numero secreto") 
    else:
        print("tu intento es mayor que el numero secreto")
print(f"adivinaste en {intentos} intentos!") # imprimimos cantidad de intentos

# ejercicio 6

for numero in range(100, -1, -2):  # itera por los numeros de 0 a 100 en pasos de 2
    print(numero) # imprime el numero de iteracion en cada vuelta

# ejercicio 7

numero = int(input("ingresa un entero positivo"))
if numero >= 0: # chequeamos si es positivo
    suma = 0 # inicializamos la suma
    for i in range(numero + 1):  # itera desde 0 hasta el num ingresado
        suma += i
    print(f"la suma de los numeros entre 0 y {numero} es {suma}")
else:
    print("el numero tiene que ser positivo") # si no es positivo, le avisamos al usuario

# ejercicio 8

totales = 100 # cantidad de numeros a ingresar
pares = 0 # contador
impares = 0 # contador
positivos = 0 # contador
negativos = 0 # contador

for i in range(totales): # iteramos x veces
    numero = int(input(f"ingresa un numero: "))  # pedimos un numero por loop
    if numero > 0:
        positivos += 1 # si es positivo, sumamos al contador
    elif numero < 0:
        negativos += 1 # si es negativo, sumamos al contador
    if numero % 2 == 0:
        pares += 1 # si es par, sumamos al contador
    else:
        impares += 1 # si es impar, sumamos al contador

print(f"hay {pares} pares")
print(f"hay {impares} impares")
print(f"hay {positivos} positivos")
print(f"hay {negativos} negativos")

# ejercicio 9

totales = 100 # cantidad de numeros a ingresar
suma = 0 # inicializamos la suma
for i in range(totales): # iteramos x veces
    numero = int(input(f"ingresa un numero: "))  # pedimos un numero por loop
    suma += numero # sumamos al acumulador
media = suma / totales # calculamos la media
print(f"la media es: {media}") # y la imprimimos

# ejercicio 10

numero = int(input("ingresa un entero: ")) # pedimos un numero al usuario
if numero < 0: # chequeamos si es negativo
    signo = -1 # si es, asignamos signo como -1
else:
    signo = 1 # si no, asignamos signo como 1
invertido = 0
while numero > 0:
    digito = numero % 10 # obtener ultimo digito
    invertido = invertido * 10 + digito # agregar digito
    numero //= 10 # eliminar digito
if signo == -1:
    invertido = -invertido # si era negativo, volvemos a hacerlo negativo
print(f"el numero invertido es: {invertido}")