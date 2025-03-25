import math

print("hola mundo!")

nombre = input("como te llamas?\n")
print(f"hola {nombre}!")
apellido = input("ingresa tu apellido\n")
edad = input("ingresa tu edad\n")
pais = input("ingresa tu pais\n")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

radio = float(input("ingresa un radio\n"))
area = math.pi * pow(radio, 2)
perim = 2 * math.pi * radio
print(f"el area es {area} y el perimetro es {perim}")

segundos = float(input("ingresa los segundos\n"))
horas = segundos // 3600
print(f"son {horas} horas")

num = float(input("ingresa el numero\n"))
for i in range (0, 11):
  print(f"{num} x {i} = {num * i}")

num1 = float(input("ingresa el primer numero\n"))
num2 = float(input("ingresa el segundo numero\n"))
print(f"la suma es {num1 + num2}")
print(f"la resta es {num1 - num2}") 
print(f"la multiplicacion es {num1 * num2}")
print(f"la division es {num1 / num2}")

altura = float(input("ingresa tu altura\n"))
peso = float(input("ingresa tu peso\n"))
imc = peso / pow(altura, 2)
print(f"tu imc es {imc}")

celcius = float(input("ingresa la temperatura en celcius\n"))
farenheit = (celcius * 9/5) + 32
print(f"la temperatura en farenheit es {farenheit}")

numA = float(input("ingresa el primer numero\n"))
numB = float(input("ingresa el segundo numero\n"))
numC = float(input("ingresa el tercer numero\n"))
promedio = (numA + numB + numC) / 3
print(f"el promedio es {promedio}")