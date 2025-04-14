# ejercicio 1

preciosFrutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450} # diccionario original
preciosFrutas["naranja"] = 1200
preciosFrutas["manzana"] = 1500
preciosFrutas["pera"] = 2300

# ejercicio 2

preciosFrutas["banana"] = 1330 # cambiamos el precio de la banana
preciosFrutas["manzana"] = 1700 # cambiamos el precio de la manzana
preciosFrutas["melon"] = 2800 # cambiamos el precio del melon

# ejercicio 3

frutas = list(preciosFrutas.keys()) # obtenemos una lista de las frutas con keys()
print(frutas)

# ejercicio 4

class persona: # creamos la clase persona
  def __init__(self, nombre, pais, edad): # inicializamos los atributos
    self.nombre = nombre
    self.pais = pais
    self.edad = edad
  def saludar(self): # creamos el metodo saludar
    print(f"hola, soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")
juan = persona("juan", "argentina", 25)
juan.saludar() # llamamos al metodo saludar de la clase persona

# ejercicio 5

from math import pi
class circulo: # creamos la clase circulo
  def __init__(self, radio): # inicializamos el radio
    self.radio = radio # inicializamos el radio
  def calcularArea(self): # creamos el metodo que calcula el area
    areaCirculo = round(pi * self.radio * self.radio, 2) # calculamos el area
    return areaCirculo # la devolvemos
  def calcularPerimetro(self): # creamos el metodo que calcula el perimetro
    perimetroCirculo = round(2 * pi * self.radio, 2) # calculamos el perimetro
    return perimetroCirculo # lo devolvemos

circuloA = circulo(6) # definimos un circulo con radio 6
print(circuloA.calcularArea()) # imprimimos la lllamada al metodo calcularArea
print(circuloA.calcularPerimetro()) # imprimimos la lllamada al metodo calcularPerimetro

# ejercicio 6

def chequearBalance(input): # definimos la funcion balanceado
    pares = {')': '(', '}': '{', ']': '['} # definimos un diccionario con los pares
    pila = [] # inicializamos la pila para sumarar los parentesis
    for signo in input: # recorremos la string
        if signo in "({[": # si el signo es de apertura
            pila.append(signo) # lo sumamos a la pila
        elif signo in ")}]": # si el signo es de cierre
            if not pila: # si la pila esta vacia
                return False # devolvemos false
            ultimo = pila.pop() # sacamos el ultimo elemento de la pila
            if ultimo != pares[signo]: # comparamos con el par
                return False # si no coincide, devolvemos false
    return len(pila) == 0 
print(chequearBalance("({[]})"))
print(chequearBalance("({})"))

#  ejercicio 7

from collections import deque
class colaTurnos: # creamos la clase colaTurnos
    def __init__(self): # inicializamos la cola
        self.cola = deque() # inicializamos la cola con deque
    def agregarCliente(self, cliente): # creamos el metodo para agregar un cliente
        self.cola.append(cliente) # agregamos el cliente a la cola
    def atenderCliente(self): # creamos el metodo para atender un cliente
        return self.cola.popleft() if self.cola else "no hay clientes" # atendemos al cliente
    def siguienteCliente(self): # creamos el metodo para ver el siguiente cliente
        return self.cola[0] if self.cola else "no hay clientes" # vemos el siguiente cliente
    
    # ejercicio 8

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class listaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar(self, dato):
        nuevo = nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
        print("none")
    
    # ejercicio 9

    def invertir(self):
        prev = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = prev
            prev = actual
            actual = siguiente
        self.cabeza = prev
lista = listaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
print("lista original:") # mostramos la lista original
lista.mostrar()
lista.invertir() # invertimos la lista
print("lista invertida:") # mostramos la lista invertida
lista.mostrar()