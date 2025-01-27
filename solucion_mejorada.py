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
    largest = second = float('-inf') # inicializamos los valores con el menor numero posible.
    for num in numbers:
        if num > largest: # si encontramos un numero mayor que el mayor actual.
            second = largest # actualizamos el segundo mas grande.
            largest = num # actualizamos el mayor con el numero actual.
        elif num > second and num != largest: # si el numero es mayor al segundo, pero no al mayor.
            second = num # actualizamos el segundo numero mas grande.
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
    def __init__(self): # constructor de la clase Inventory
        self.products = {} # dicionario que almacena los productos

    def add(self, name, quantity, price): # parametros de entrada de producto
        """Agrega un producto al inventario."""
        if name in self.products: # control de duplicados
            raise ValueError(f"El producto '{name}' ya existe.")
        self.products[name] = {'quantity': quantity, 'price': price} # almacena cantidad y precio

    def update(self, name, quantity):
        """Actualiza la cantidad de un producto existente."""
        if name not in self.products: # valida su existencia
            raise ValueError(f"El producto '{name}' no existe.")
        self.products[name]['quantity'] += quantity # suma la nueva cantidad

    def inventory_value(self): # calcula el valor total del inventario
        """Calcula el valor total del inventario."""
        #retorna el valor total del inventario
        return sum(item['quantity'] * item['price'] for item in self.products.values())

    def display_inventory(self):
        """Muestra el inventario en formato de tabla."""
        print("\nInventario actual:")
         # encabezados de la tabla con formato especifico para alinear columnas.
        print(f"{'Producto':<15}{'Cantidad':<10}{'Precio Unitario':<15}{'Valor Total':<10}")
        print("-" * 50) # linea de division
        # itera sobre el inventario para mostrar cada producto
        for name, details in self.products.items():
            total_value = details['quantity'] * details['price'] # Calcula el valor total de cada producto.
            # imprime los detalles del producto con formato para alinearlos en la tabla.
            print(f"{name:<15}{details['quantity']:<10}{details['price']:<15}{total_value:<10}")
        print("-" * 50) # linea final

# 5. Generar una tabla de multiplicar.
def multiplication_table(number, limit=10):
    """Genera la tabla de multiplicar para un numero hasta el limite especificado."""
   # usa la comprension de listas para crear la tabla de multiplicar
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]

#########################################
# Sección 3: Pregunta abierta de lógica #
#########################################

# 6. Razonamiento lógico aplicado (tren y estaciones).
def train_passenger_count(events):
    """Calcula el número de pasajeros en el tren después de cada estación."""
    passengers = 0
    for i, event in enumerate(events, start=1):  # itera por cada estacion.
        # - 'in': numero de pasajeros que suben al tren.
        # - 'out': numero de pasajeros que bajan del tren.
        passengers += event['in'] - event['out'] # actualiza el numero de pasajeros en funcion de los eventos.
        # imprime los detalles de la estacion.
        print(f"Estación {i}: Subieron {event['in']} pasajeros, Bajaron {event['out']} pasajeros.")
        
        # valida si el numero de pasajeros es negativo.if passengers < 0:
        raise ValueError("El número de pasajeros no puede ser negativo.")
    # imprime el total de pasajeros al final del recorrido.
    print(f"Al final del recorrido, en el tren hay {passengers} pasajeros.")
    return passengers # Retorna el número total de pasajeros

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
    print("\n--- EJERCICIO 1: ORDENAR POR LONGITUD ---")
    entrada_ej1 = ["manzana", "perro", "hola", "extraordinario"]
    print(f"Entrada: {entrada_ej1}")
    print(f"Salida: {sort_by_length(entrada_ej1)}")

    print("\n--- EJERCICIO 2: SEGUNDO NÚMERO MÁS GRANDE ---")
    entrada_ej2 = [10, 20, 30, 40, 50]
    print(f"Entrada: {entrada_ej2}")
    print(f"Salida: {second_largest(entrada_ej2)}")

    print("\n--- EJERCICIO 3: BALANCEO DE PARÉNTESIS ---")
    entradas_ej3 = ["(a + b) * (c - d)", "(a + b) * (c - d))"]
    for caso in entradas_ej3:
        print(f"Caso: '{caso}' - {is_balanced_parentheses(caso)}")

    print("\n--- EJERCICIO 4: GESTIÓN DE INVENTARIO ---")
    inventory = Inventory()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar cantidad")
        print("3. Mostrar valor total del inventario")
        print("4. Mostrar inventario en tabla")
        print("5. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: "))
            try:
                inventory.add(nombre, cantidad, precio)
                print(f"Producto '{nombre}' agregado correctamente.")
            except ValueError as e:
                print(e)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a agregar: "))
            try:
                inventory.update(nombre, cantidad)
                print(f"Cantidad de '{nombre}' actualizada correctamente.")
            except ValueError as e:
                print(e)
        elif opcion == "3":
            print(f"Valor total del inventario: {inventory.inventory_value()}")
        elif opcion == "4":
            inventory.display_inventory()
        elif opcion == "5":
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

    print("\n--- EJERCICIO 5: TABLA DE MULTIPLICAR ---")
    numero = int(input("Número para la tabla de multiplicar: "))
    limite = input("Hasta qué número multiplicar (por defecto 10): ")
    limite = int(limite) if limite.isdigit() else 10
    print("\n".join(multiplication_table(numero, limite)))

    print("\n--- EJERCICIO 6: PASAJEROS EN EL TREN ---")
    eventos_ej6 = [
        {"in": 3, "out": 0},
        {"in": 2, "out": 1},
        {"in": 0, "out": 2}
    ]
    train_passenger_count(eventos_ej6)



