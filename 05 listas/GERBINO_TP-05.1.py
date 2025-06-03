# ejercicio uno

listaMultiplos = list(range(4, 101, 4)) # creamos una lista con los multiplos de cuatro
print(listaMultiplos) # imprimimos la lista

# ejercicio dos

listaColores =  ["rojo", "verde", "azul", "amarillo", "naranja"] # creamos una lista con los colores
print('el penultimo elemento es: ' + listaColores[-2]) # imprimimos el penultimo elemento de la lista

# ejercicio tres

listaPalabras = [] # creamos una lista vacia
listaPalabras.append('hola') # agregamos la palabra hola a la lista
listaPalabras.append('adios') # agregamos la palabra adios a la lista
listaPalabras.append('chau') # agregamos la palabra chau a la lista
print(listaPalabras) # imprimimos la lista

# ejercicio cuatro

animales = ['perro', 'gato', 'tortuga', 'pez'] # creamos una lista con los animales
animales[1] = 'loro' # cambiamos el segundo elemento de la lista por loro
animales[-1] = 'oso' # cambiamos el ultimo elemento de la lista por oso
print(animales) # imprimimos la lista

# ejercicio cinco

## el programa crea una lista llamada numeros, con los valores: 8, 15, 3, 22, 7
## encuentra el valor maximo pasando la lista a la funcion max(), el resultado es 22
## elimina el valor maximo de la lista con el metodo remove()
## imprime la lista resultante, que sera [8, 15, 3, 7]

# ejercicio seis

listaNumeros = list(range(10, 31, 5)) # creamos una lista con los numeros del 10 al 30, saltando de a 5
print('los dos primeros numeros son: ' + listaNumeros[:2]) # imprimimos los dos primeros numeros de la lista

# ejercicio siete

listaAutos = ["sedan", "polo", "suran", "gol"] # creamos una lista con los autos
listaAutos[1] = "fiesta" # cambiamos el segundo elemento de la lista por fiesta
listaAutos[3] = "focus" # cambiamos el cuarto elemento de la lista por focus
print(listaAutos) # imprimimos la lista

# ejercicio ocho

listaDobles = [] # creamos una lista vacia
listaDobles.append(5 * 2) # agregamos el doble de 5 a la lista
listaDobles.append(10 * 2) # agregamos el doble de 10 a la lista
listaDobles.append(15 * 2) # agregamos el doble de 15 a la lista
print(listaDobles) # imprimimos la lista

# ejercicio nueve

listaCompras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] # definimos la lista de compras
listaCompras[2].append("jugo") # agregamos jugo a la tercera lista
listaCompras[1][1] = "tallarines" # cambiamos el segundo elemento de la segunda lista por tallarines
listaCompras[0].remove("pan") # cambiamos el primer elemento de la lista por jugo
print(listaCompras) # imprimimos la lista

# ejercicio diez

listaAnidada = [15, True, [25.5, 57.9, 30.6], False] # definimos la lista anidada
print(listaAnidada) # imprimimos la lista