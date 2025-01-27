# Prueba Técnica: Evaluación de Lógica y Programación
# Autor: Oscar Camilo Calle Gil
# Lenguaje: Python
# Descripción: Elegi Python por que es un lenguaje legible, tiene mucha facilidad de uso y es eficiente para resolver problemas de lógica, ademas de su facil ejecucion.
# Herramientas: Use Visual Studio Code como IDE.

##################################
# Sección 1: Lógica y Algoritmos #
##################################

# 1. Ordenar un arreglo de strings por su longitud.
def sort_by_length(strings):
    """Ordenar un arreglo de strings por su longitud."""
    return sorted(strings, key=len)

# Ejemplo de entrada y salida:
# Entrada: ["manzana", "perro", "hola", "extraordinario"]
# Salida: ["hola", "perro", "manzana", "extraordinario"]

# 2. Encontrar el segundo número más grande (sin usar sort).
def second_largest(numbers):
    """Encontrar el segundo número más grande."""
    if len(numbers) < 2:
        raise ValueError("El arreglo debe tener al menos dos numeros.")
    largest = second = float('-inf') # Inicializamos los valores con el menor nmero posible.
    for num in numbers:
        if num > largest: # Si encontramos un numero mayor que el mayor actual.
            second = largest # Actualizamos el segundo mas grande.
            largest = num # Actualizamos el mayor con el numero actual.
        elif num > second and num != largest: # Si el numero es mayor al segundo, pero no al mayor.
            second = num # Actualizamos el segundo numero mas grande.
    return second

# Ejemplo de entrada y salida:
# Entrada: [10, 20, 30, 40, 50]
# Salida: 40

# 3. Balanceo de paréntesis.
def is_balanced_parentheses(string):
    """Verificar si los parentesis estan balanceados en una cadena."""
    balance = 0 # lleva el conteo del balance de los aprentesis
    for char in string:
        if char == '(':
            balance += 1 # incrementa pro cada parentesis abierto
        elif char == ')':
            balance -= 1 # decrementa por parentesis cerrado
        if balance < 0: # verifica si el balance es negativo significa que hay mas cerrados
            return False
    return balance == 0

# Ejemplo de entrada y salida:
# Entrada: "(a + b) * (c - d)"
# Salida: True
# Entrada: "(a + b) * (c - d))"
# Salida: False

################################################
# Sección 2: Resolución de problemas prácticos #
################################################

# 4. Sistema de gestión de inventario
class Inventory:
    def __init__(self):
        self.products = {} # dicionario que almacena los productos

    def add(self, name, quantity, price):
        """Agrega un producto al inventario."""
        if name in self.products: # control de duplicados
            raise ValueError(f"El producto '{name}' ya existe.")
        self.products[name] = {'quantity': quantity, 'price': price} # almacena cantidad y precio

    def update(self, name, quantity):
        """Actualiza la cantidad de un producto existente."""
        if name not in self.products: # valida su existencia
            raise ValueError(f"El producto '{name}' no existe.")
        self.products[name]['quantity'] += quantity # suma la nueva cantidad

    def inventory_value(self):
        """Calcula el valor total del inventario."""
        # comprende las listas para cualcular cantidad * precio de cada producto
        return sum(item['quantity'] * item['price'] for item in self.products.values())

# Ejemplo de uso:
# inventory = Inventory()
# inventory.add("manzanas", 10, 2.5)
# inventory.update("manzanas", 5)
# print("Valor total:", inventory.inventory_value())  # Salida: 37.5

# 5. Generar una tabla de multiplicar.
def multiplication_table(number):
    """Genera la tabla de multiplicar para un numero hasta el 10."""
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]

# Ejemplo de entrada y salida:
# Entrada: numero = 7
# Salida:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

#########################################
# Sección 3: Pregunta abierta de lógica #
#########################################

# 6. Razonamiento lógico aplicado (tren y estaciones).
def train_passenger_count(events):
    """Calcula el número de pasajeros en el tren después de cada estación."""
    passengers = 0
    for event in events:
        passengers += event['in'] - event['out']
        if passengers < 0:
            raise ValueError("El número de pasajeros no puede ser negativo.")
    return passengers

# Ejemplo de entrada y salida:
# Entrada: [
#     {"in": 3, "out": 0},
#     {"in": 2, "out": 1},
#     {"in": 0, "out": 2}
# ]
# Salida: 2

#############################
# Insrucciones de ejecucion #
#############################
# 1. tener Python instalado (versión 3.7 o superior).
# 2. Guarda este archivo como `solucion_simple.py`.
# 3. Abrir una terminal y ejecuta: `python solucion_simple.py`.
# 4. Modifica las llamadas a las funciones o instancias para probar diferentes casos.

#########
# Tests #
#########
if __name__ == "__main__":
    # Test Sección 1
    print("\n1. Ordenar arreglo por longitud:")
    print(sort_by_length(["manzana", "perro", "hola", "extraordinario"]))

    print("\n2. Encontrar el segundo número más grande:")
    print(second_largest([10, 20, 30, 40, 50]))

    print("\n3. Verificar balance de paréntesis:")
    print("Caso 1:", is_balanced_parentheses("(a + b) * (c - d)"))
    print("Caso 2:", is_balanced_parentheses("(a + b) * (c - d))"))

    # Test Inventario
    print("\n4. Sistema de gestión de inventario:")
    inventory = Inventory()
    inventory.add("manzanas", 10, 2.5)
    inventory.update("manzanas", 5)
    print("Valor total:", inventory.inventory_value())

    # Test Tabla de multiplicar
    print("\n5. Generar tabla de multiplicar:")
    print("\n".join(multiplication_table(7)))

    # Test Tren
    print("\n6. Razonamiento lógico aplicado (tren y estaciones):")
    events = [
        {"in": 3, "out": 0},
        {"in": 2, "out": 1},
        {"in": 0, "out": 2}
    ]
    print("Pasajeros finales:", train_passenger_count(events))