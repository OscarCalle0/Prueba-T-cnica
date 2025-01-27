# Prueba Técnica: Evaluación de Lógica y Programación

## Autor
Oscar Camilo Calle Gil

## Lenguaje Utilizado
**Python**
- Elegí Python por su legibilidad, facilidad de uso, y eficiencia en la resolución de problemas de lógica.
- Es un lenguaje versátil con una comunidad amplia, lo que facilita encontrar recursos y soporte.

## Herramientas Utilizadas
- **IDE:** Visual Studio Code (VS Code).

---

## Ejercicios Resueltos

### **Sección 1: Lógica y Algoritmos**

1. **Ordenar un arreglo de strings por su longitud**
   - Funcionalidad: Ordena un arreglo de strings de menor a mayor según su longitud.
   - Ejemplo de entrada:
     ```python
     ["manzana", "perro", "hola", "extraordinario"]
     ```
   - Salida esperada:
     ```python
     ["hola", "perro", "manzana", "extraordinario"]
     ```

2. **Encontrar el segundo número más grande**
   - Funcionalidad: Encuentra el segundo número más grande en un arreglo sin usar funciones predefinidas como `sort`.
   - Ejemplo de entrada:
     ```python
     [10, 20, 30, 40, 50]
     ```
   - Salida esperada:
     ```python
     40
     ```

3. **Balanceo de paréntesis**
   - Funcionalidad: Verifica si una cadena tiene los paréntesis correctamente balanceados.
   - Ejemplo de entrada:
     ```python
     "(a + b) * (c - d)"
     ```
   - Salida esperada:
     ```python
     True
     ```

### **Sección 2: Resolución de Problemas Prácticos**

4. **Sistema de gestión de inventario**
   - Funcionalidad: Simula un sistema básico de inventario que permite:
     - Agregar productos.
     - Actualizar la cantidad de productos existentes.
     - Calcular el valor total del inventario.
   - Ejemplo de entrada:
     ```python
     inventory = Inventory()
     inventory.add("manzanas", 10, 2.5)
     inventory.update("manzanas", 5)
     inventory.inventory_value()
     ```
   - Salida esperada:
     ```python
     Valor total: 37.5
     ```

5. **Generar una tabla de multiplicar**
   - Funcionalidad: Genera la tabla de multiplicar para un número dado hasta el 10.
   - Ejemplo de entrada:
     ```python
     numero = 7
     ```
   - Salida esperada:
     ```python
     ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 10 = 70"]
     ```

### **Sección 3: Pregunta Abierta de Lógica**

6. **Razonamiento lógico aplicado (tren y estaciones)**
   - Funcionalidad: Calcula el número de pasajeros en el tren después de cada estación, basado en un registro de eventos (subidas y bajadas).
   - Ejemplo de entrada:
     ```python
     events = [
         {"in": 3, "out": 0},
         {"in": 2, "out": 1},
         {"in": 0, "out": 2}
     ]
     ```
   - Salida esperada:
     ```python
     Pasajeros finales: 2
     ```

---

## Instrucciones para la Ejecución

1. **Instalación de Dependencias**
   - Asegúrate de tener Python 3.7 o superior instalado. Puedes verificar la versión ejecutando:
     ```bash
     python --version
     ```

2. **Ejecución del Programa**
   - Guarda el código en un archivo llamado `solucion_simple.py`.
      Guarda el código en un archivo llamado `solucion_mejorada.py`.
   - Abre una terminal y navega al directorio donde se encuentra el archivo.
   - Ejecuta el programa con:
     ```bash
     python solucion_simple.py
     python solucion_mejorada.py
     ```

3. **Pruebas**
   - El programa incluye casos de prueba automáticos al final del archivo. Puedes modificar los ejemplos para probar diferentes entradas y salidas.

---

## Criterios de Evaluación

1. **Correctitud:** Cada solución cumple con los requisitos del problema.
2. **Eficiencia:** Las soluciones han sido diseñadas para ser eficientes.
3. **Legibilidad:** Uso de nombres de variables descriptivos y comentarios para secciones complejas.
4. **Innovación:** Se emplearon métodos lógicos y soluciones elegantes cuando fue posible.

---

Gracias por la oportunidad de participar en esta evaluación.

