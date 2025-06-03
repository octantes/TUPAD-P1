# ejercicio 1

precios_frutas = { 'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450 }
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f"estos son los {precios_frutas} originales")

# ejercicio 2

precios_frutas['Banana'] = 1300
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(f"estos son los {precios_frutas} actualizados")

# ejercicio 3

print(f"estas son solo las frutas {precios_frutas.keys()}")

# ejercicio 4

dicc_contactos = {}
for i in range(5):
  nombre  = input("ingrese un nombre: ")
  numero = input("ingrese un numero: ")
  dicc_contactos[nombre] = numero
print(f"esta es tu agenda: {dicc_contactos}")
x = input("ingrese un nombre a buscar: ")
print(f"el numero de {x} es {dicc_contactos[x]}")

# ejercicio 5

dicc_palabras = {}
frase = input("ingrese una frase: ")
for palabra in frase.split():
  if palabra in dicc_palabras:
    dicc_palabras[palabra] += 1
  else:
    dicc_palabras[palabra] = 1
print(f"este es el recuento de palabras de tu frase: {dicc_palabras}")

# ejercicio 6

dicc_alumnos = {}
for x in range (3):
  nom = input('ingrese el nombre del alumno: ')
  nota1 = input('ingrese la nota 1: ')
  nota2 = input('ingrese la nota 2: ')
  nota3 = input('ingrese la nota 3: ')
  dicc_alumnos[nom] = (nota1, nota2, nota3)
print(f"este es tu diccionario de alumnos {dicc_alumnos}")

for nombre, notas in dicc_alumnos.items():
    promedio = (float(notas[0]) + float(notas[1]) + float(notas[2])) / 3
    print(f"el promedio de {nombre} es {promedio:.2f}")

# ejercicio 7

parcial1 = {"ana", "juan", "pedro", "lucia"}
parcial2 = {"pedro", "lucia", "sofia", "marcos"}
ambos = parcial1 & parcial2
soloUno = parcial1 ^ parcial2
alMenosUno = parcial1 | parcial2
print(f"estudiantes que aprobaron ambos parciales: {ambos}")
print(f"estudiantes que aprobaron solo uno de los dos parciales: {soloUno}")
print(f"estudiantes que aprobaron al menos un parcial: {alMenosUno}")

# ejercicio 8

stock = {
    "arroz": 10,
    "fideos": 20,
    "azucar": 15,
    "leche": 8,
}

producto = input("ingrese el nombre de un producto: ")
if producto in stock:
    print(f"el stock de {producto} es {stock[producto]}")
    agregar = input("agregar unidades? (s/n): ")
    if agregar.lower() == "s":
        unidades = int(input("cuantas? "))
        stock[producto] += unidades
        print(f"nuevo stock de {producto}: {stock[producto]}")
else:
    print("el producto no existe")
    nuevo = int(input("ingrese el stock inicial para este producto: "))
    stock[producto] = nuevo
    print(f"producto {producto} agregado con stock {nuevo}")

print(f"stock actual: {stock}")

# ejercicio 9

agenda = {
    ("lunes", "10:00"): "reunion",
    ("martes", "14:00"): "clase",
    ("miercoles", "18:00"): "gym",
}

dia = input("ingrese el dia: ")
hora = input("ingrese la hora: ")
tupla = (dia, hora)
if tupla in agenda:
    print(f"el {dia} a las {hora} hay: {agenda[tupla]}")
else:
    print("no hay ningun evento agendado en ese dia y hora")

# ejercicio 10

capitalesPaises = {}
paisesCapitales = {
    "argentina": "buenos aires",
    "brasil": "brasilia",
    "chile": "santiago",
    "uruguay": "montevideo",
    "paraguay": "asuncion",
}

for pais, capital in paisesCapitales.items():
    capitalesPaises[capital] = pais
print(f"este es el diccionario invertido: {capitalesPaises}")