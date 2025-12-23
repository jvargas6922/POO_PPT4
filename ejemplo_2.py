"""
Vas a implementar una clase base Persona y una subclase Empleado que herede de ella y agregue
comportamiento específico.
🔹 Qué debe tener la clase Persona:
    ● Atributos: nombre, edad
    ● Método: presentarse() que imprima una presentación básica
🔹 Qué debe tener la subclase Empleado:
    ● Atributo adicional: cargo
    ● Método sobrescrito presentarse() que además incluya el cargo
    ● Método adicional: trabajar() que imprima lo que hace
🔹 Qué se debe probar:
    ● Crear una instancia de Empleado
    ● Verificar que puede usar métodos heredados y propios
    ● Llamar a presentarse() y observar cómo cambia el comportamiento

****************************************************************************

Ejemplo modificados:
🔹 Qué debe tener la clase Dispositivo_electronico:
    ● Atributos: voltaje, marca, tamanio, modelo
    ● Método: encender() que imprima los datos del dispositivo encendido
🔹 Qué debe tener la subclase Tablet:
    ● Atributo adicional: tamanio_pantalla
    ● Método sobrescrito encender() que además incluya el tamaño de pantalla
    ● Método adicional: conectarse_internet() que imprima el proceso de conectarse a internet
🔹 Qué debe tener la subclase Consola:
    ● Atributo adicional: cantidad_controles
    ● Método sobrescrito encender() que además incluya la cantidad de controles
    ● Método adicional: jugar() que imprima el juego que se está jugando
🔹 Qué se debe probar:
    ● Crear una instancia de Dispositivo_electronico, Tablet y Consola 
    ● Verificar que puede usar métodos heredados y propios
    ● Llamar a encender() y observar cómo cambia el comportamiento
"""

class Dipositivo_electronico:
    # contructor
    def __init__(self, voltaje, marca, tamanio, modelo):
        self.voltaje = voltaje
        self.marca = marca
        self.tamanio = tamanio
        self.modelo = modelo

    def encender(self):
        print(f"Dispositivo encendido: {self.marca} {self.modelo}, Voltaje: {self.voltaje}V, Tamaño: {self.tamanio}")



class Tablet(Dipositivo_electronico):
    def __init__(self, voltaje, marca, tamanio, modelo, tamanio_pantalla):
        super().__init__(voltaje, marca, tamanio, modelo)
        self.tamanio_pantalla = tamanio_pantalla

    def jugar(self):
        super().encender()
        print(f"Tamaño de pantalla: {self.tamanio_pantalla} pulgadas")


    def conectarse_internet(self):
        print("Conectándose a internet...")




class Consola(Dipositivo_electronico):
    def __init__(self, voltaje, marca, tamanio, modelo, cantidad_controles):
        super().__init__(voltaje, marca, tamanio, modelo)
        self.cantidad_controles = cantidad_controles

    def encender(self):
        super().encender()
        print(f"Cantidad de controles: {self.cantidad_controles}")

    def jugar(self):
        print("Jugando en la consola... Call Of Duty")

# creacion de instancias

print("Sistema para la creacion de dispositivos electronicos\n")
dispositivos = []
opciones = ['dispositivo', 'tablet', 'consola', 'salir']

while True:
    opcion = input(f"Seleccione una opción ({', '.join(opciones)}): ").lower()
    # validar que la opcion esta contenida en las opciones
    if opcion not in opciones:
        print("Opción no válida. Intente de nuevo.")
        continue
    elif opcion == 'salir':
        print("Saliendo del sistema.")
        break
    elif opcion == 'dispositivo':
        # voltaje, marca, tamanio, modelo
        voltaje = input("Ingrese el voltaje del dispositivo: ")
        marca = input("Ingrese la marca del dispositivo: ")
        tamanio = input("Ingrese el tamaño del dispositivo: ")
        modelo = input("Ingrese el modelo del dispositivo: ")
        dispositivo = Dipositivo_electronico(voltaje, marca, tamanio, modelo)
        dispositivos.append(dispositivo)
        print("Dispositivo electrónico creado exitosamente.\n")
    elif opcion == 'tablet':
        voltaje = input("Ingrese el voltaje de la tablet: ")
        marca = input("Ingrese la marca de la tablet: ")
        tamanio = input("Ingrese el tamaño de la tablet: ")
        modelo = input("Ingrese el modelo de la tablet: ")
        tamanio_pantalla = input("Ingrese el tamaño de pantalla de la tablet (en pulgadas): ")
        tablet = Tablet(voltaje, marca, tamanio, modelo, tamanio_pantalla)
        dispositivos.append(tablet)
        print("Tablet creada exitosamente.\n")
    elif opcion == 'consola':
        voltaje = input("Ingrese el voltaje de la consola: ")
        marca = input("Ingrese la marca de la consola: ")
        tamanio = input("Ingrese el tamaño de la consola: ")
        modelo = input("Ingrese el modelo de la consola: ")
        cantidad_controles = input("Ingrese la cantidad de controles de la consola: ")
        consola = Consola(voltaje, marca, tamanio, modelo, cantidad_controles)
        dispositivos.append(consola)
        print("Consola creada exitosamente.\n")

# probar los metodos
for dispositivo in dispositivos:
    print("\nProbando dispositivo:")
    dispositivo.encender()
    if isinstance(dispositivo, Tablet):
        dispositivo.conectarse_internet()
    if isinstance(dispositivo, Consola):
        dispositivo.jugar()





