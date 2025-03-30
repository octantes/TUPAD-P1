from statistics import mode, median, mean
import random

# uno
edad = int(input("por favor, ingresa tu edad: "))
if edad > 18:
    print("sos mayor de edad")
else:
    print("no sos mayor de edad")

# dos
nota = float(input("por favor, ingresa tu nota: "))
if nota >= 6:
    print("aprobaste")
else:
    print("desaprobaste")

# tres
par = int(input("por favor, ingresa un numero par: "))
if par % 2 == 0:
    print("el numero es par")
else:
    print("por favor, ingresa un numero par")

# cuatro
años = int(input("por favor, ingresa tu edad: "))
if años >= 30:
    print("sos un adulto")
elif años >= 18 and años < 30:
    print("sos un adulto joven")
elif años >= 12 and años < 18:
    print("sos un adolescente")
else:
    print("sos un niño")

# cinco
contraseña = input("por favor, ingresa tu contraseña: ")
contraseñaLength = len(contraseña)
if contraseñaLength >= 8 and contraseñaLength <= 14:
    print("la contraseña es segura")
else:
    print("la contraseña es insegura")

# seis
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"la mediana es: {mediana}")
print(f"la moda es: {moda}")
print(f"la media es: {media}")
if media > mediana and mediana > moda:
    print("sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("sin sesgo")

# siete
frase = input("por favor, ingresa una frase o palabra: ")
letraFinal = frase[-1]
if letraFinal == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
    print(frase + "!")
else:
    print(frase)

# ocho
nombre = input("por favor, ingresa tu nombre: ")
eleccion = int(input("1 para mayusculas, 2 para minusculas, 3 para la primera letra en mayuscula: "))
if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2:
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.title())
else:
    print("opcion no valida")

# nueve
magnitud = float(input("por favor, ingresa la magnitud del terremoto: "))
if magnitud >= 0 and magnitud < 3:
    print("muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("leve")
elif magnitud >= 4 and magnitud < 5:
    print("moderado")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("muy fuerte")
elif magnitud >= 7:
    print("extremo")

# diez
hemisferio = input("por favor, ingresa el hemisferio: ")
mes = int(input("por favor, ingresa el mes en numero: "))
dia = int(input("por favor, ingresa el dia: "))
if hemisferio == "n":
  if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "es invierno"
  elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "es primavera"
  elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "es verano"
  elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "es otoño"
elif hemisferio == "s":
  if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "es verano"
  elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "es otoño"
  elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "es invierno"
  elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "es primavera"
else:
  estacion = "hemisferio no valido"
print(estacion)