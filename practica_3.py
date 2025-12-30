"""
Portal inmuliario nos contrata para poder crear inmuebles en un su portal web.
Consigna tu como desarrollador debes permitrile al usuario poder crear inmuebles y luego mostrar la informacion de los mismos.
- cosas a tener en cuenta debes validar la entrada de datos y la llamada de los metodos propios de cada clase.

clase base para Inmuebles
    Atributos:
        - direccion: str
        - metros_cuadrados: float
        - precio: float

    info_propiedad()->str

clase Casa
    Atributos:
        - tipo_casa: str
        - cantidad_habitaciones: int
        - cantidad_banio: int
        - patio: bool

    info_propiedad()->str
    ir_jardin()->str

clase Departamento
    Atributos:
        - piso: int
        - bodega: bool
        - estacionamiento: bool
    info_propiedad()->str
    ir_terraza()->str
"""
class Inmueble:
    def __init__(self, direccion:str, metros_cuadrados:float, precio:float ):
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.precio = precio

    def info_propiedad(self)->str:
        return f"Direccion: {self.direccion}, Metros Cuadrados: {self.metros_cuadrados}, Precio: {self.precio}" 

class Casa(Inmueble): 
    def __init__(self, direccion:str, metros_cuadrados:float, precio:float, tipo_casa:str, cantidad_habitaciones:int, cantidad_banio:int, patio:bool):
        super().__init__(direccion, metros_cuadrados, precio)
        self.tipo_casa = tipo_casa
        self.cantidad_habitaciones = cantidad_habitaciones
        self.cantidad_banio = cantidad_banio
        self.patio = patio

    def info_propiedad(self)->str:
        patio_str = "Si" if self.patio else "No"
        return f"{super().info_propiedad()}, Tipo de Casa: {self.tipo_casa}, Habitaciones: {self.cantidad_habitaciones}, Baños: {self.cantidad_banio}, Patio: {patio_str}"

    def ir_jardin(self)->str:
        if self.patio:
            return "Disfrutando del jardín."
        else:
            return "Esta casa no tiene jardín."
        
class Departamento(Inmueble):
    def __init__(self, direccion:str, metros_cuadrados:float, precio:float, piso:int, bodega:bool, estacionamiento:bool):
        super().__init__(direccion, metros_cuadrados, precio)
        self.piso = piso
        self.bodega = bodega
        self.estacionamiento = estacionamiento

    def info_propiedad(self)->str:
        bodega_str = "Si" if self.bodega else "No"
        estacionamiento_str = "Si" if self.estacionamiento else "No"
        return f"{super().info_propiedad()}, Piso: {self.piso}, Bodega: {bodega_str}, Estacionamiento: {estacionamiento_str}"

    def ir_terraza(self)->str:
        return f"Subiendo al piso {self.piso} para disfrutar de la terraza."
    

# implementacion del sistema de creacion de inmuebles.
print("Sistema para la creacion de inmuebles\n")
inmuebles = []
opciones = ['inmueble', 'casa', 'departamento', 'salir']
while True:
    opcion = input(f"Seleccione una opción ({', '.join(opciones)}): ").lower()
    if opcion not in opciones:
        print("Opción no válida. Intente de nuevo.")
        continue

    elif opcion == 'salir':
        print("Saliendo del sistema.")
        break

    elif opcion == 'inmueble':
        # direccion, metros_cuadrado, precio
        direccion = input("Ingrese la direccion del inmueble: ")
        metros_cuadrado = input("Ingrese los metros cuadrados del inmueble: ")
        precio = input("Ingrese el precio del inmueble: ")
        inmueble = Inmueble(direccion,metros_cuadrado, precio)
        inmuebles.append(inmueble)
        print("Inmueble creado exitosamente.\n")

    elif opcion == 'casa':
        # direccion, metros_cuadrado, precio, tipo_casa, cantidad_habitaciones, cantidad_banio, patio): 
        direccion = input("Ingrese la direccion del inmueble: ")
        metros_cuadrado = input("Ingrese los metros cuadrados del inmueble: ")
        precio = input("Ingrese el precio del inmueble: ")

        # atributos propios de casa
        tipo_casa = input("Ingrese el tipo de casa (ej. 'Independiente', 'Adosada'): ")
        cantidad_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
        cantidad_banio = int(input("Ingrese la cantidad de baños: "))
        patio_input = input("¿Tiene patio? (si/no): ").lower()
        patio = True if patio_input == 'si' else False
        inmueble = Casa(direccion,metros_cuadrado, precio, tipo_casa, cantidad_habitaciones, cantidad_banio, patio)
        inmuebles.append(inmueble)
        print("Casa creada exitosamente.\n")

    elif opcion == 'departamento':
        # direccion, metros_cuadrado, precio, piso, bodega, estacionamiento
        direccion = input("Ingrese la direccion del inmueble: ")
        metros_cuadrado = input("Ingrese los metros cuadrados del inmueble: ")
        precio = input("Ingrese el precio del inmueble: ")

        # atributos propios de departamento
        piso = int(input("Ingrese el piso del departamento: "))
        bodega_input = input("¿Tiene bodega? (si/no): ").lower()
        bodega = True if bodega_input == 'si' else False
        estacionamiento_input = input("¿Tiene estacionamiento? (si/no): ").lower()
        estacionamiento = True if estacionamiento_input == 'si' else False
        inmueble = Departamento(direccion,metros_cuadrado, precio, piso, bodega, estacionamiento)
        inmuebles.append(inmueble)
        print("Departamento creado exitosamente.\n")

    # probar los metodos
for inmueble in inmuebles:
    print("\nInformación del inmueble:")
    print(inmueble.info_propiedad())
    if isinstance(inmueble, Casa):
        print(inmueble.ir_jardin())
    if isinstance(inmueble, Departamento):
        print(inmueble.ir_terraza())