# ejercicio 1

def printHolaMundo(): # definimos la funcion
    print("hola mundo!") # imprimimos el mensaje
printHolaMundo()

# ejercicio 2

def saludar(nombre): # definimos la funcion
    return f"hola {nombre}!" # imprimimos el mensaje
nombre = input("ingresa tu nombre: ") # pedimos el nombre
print(saludar(nombre)) # llamamos la funcion

# ejercicio 3

nombre = input("como te llamas?")
apellido = input("cual es tu apellido?")
edad = input("cuantos años tenes?")
residencia = input("de donde sos?")
def infoPersonal(nombre, apellido, edad, residencia): # definimos la funcion
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") # imprimimos mensaje
infoPersonal(nombre, apellido, edad, residencia)

# ejercicio 4

pi = 3.14
radio = float(input("ingresa el radio"))
def areaCirculo(radio): # definimos la funcion para el area
    return pi * radio ** 2 # calculamos el area
def perimetroCirculo(radio): # definimos la funcion para el perimetro
    return 2 * pi * radio # calculamos el perimetro
area = areaCirculo(radio)
perimetro = perimetroCirculo(radio)
print(f"el area es: {area}")
print(f"el perimetro es: {perimetro}") # imprimimos los resultados

# ejercicio 5
segundos = float(input("ingresa los segundos"))
def segundosHoras(segundos): # definimos la funcion
    return segundos / 3600 # convertimos segundos a horas
horas = segundosHoras(segundos)
print(f"{segundos} segundos son {horas} horas") # imprimimos el resultado

# ejercicio 6

def tablaMultiplicar(numero): # definimos la funcion
    print(f"tabla de multiplicar de {numero}")
    for i in range(1, 11): # iteramos del 1 al 10
        print(f"x{i} = {numero * i}") # imprimimos la tabla
numero = int(input("que tabla queres?")) # pedimos el numero
tablaMultiplicar(numero)

# ejercicio 7

numA = float(input("ingresa el primer numero")) # pedimos el primer numero
numB = float(input("ingresa el segundo numero")) # pedimos el segundo numero
def operacionesBasicas(numA, numB): # definimos la funcion
    suma = numA + numB
    resta = numA - numB
    multiplicacion = numA * numB
    division = numA / numB
    return (suma, resta, multiplicacion, division) # calculamos las operaciones
resultados = operacionesBasicas(numA, numB) # llamamos la funcion
print(f"la suma es: {resultados[0]}")
print(f"la resta es: {resultados[1]}")
print(f"la multiplicacion es: {resultados[2]}")
print(f"la division es: {resultados[3]}")

# ejercicio 8

def calcularIMC(peso, altura): # definimos la funcion
    return peso / (altura ** 2) # calculamos el IMC
peso = float(input("ingresa peso en kg")) # pedimos el peso
altura = float(input("ingresa altura en mts")) # pedimos la altura
imc = calcularIMC(peso, altura) # llamamos la funcion
print(f"tu IMC es {imc}")

# ejercicio 9

def celsiusFarenheit(celsius): # definimos la funcion
    return (celsius * 9/5) + 32 # convertimos celsius a fahrenheit
celsius = float(input("ingrese la temperatura en celsius")) # pedimos la temperatura
fahrenheit = celsiusFarenheit(celsius) # llamamos la funcion
print(f"{celsius}°c equivalen a {fahrenheit}°f") # imprimimos el resultado

# ejercicio 10

def calcularPromedio(a, b, c): # definimos la funcion
    return (a + b + c) / 3  # calculamos el promedio
num1 = float(input("ingresa el primer numero"))
num2 = float(input("ingresa el segundo numero"))
num3 = float(input("ingresa el tercer numero"))
promedio = calcularPromedio(num1, num2, num3) # llamamos la funcion
print(f"el promedio es: {promedio}")