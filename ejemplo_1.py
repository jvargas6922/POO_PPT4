"""
Ejemplo de Herencia en Python.

crear un ejemplo de herencia en python con las clases computadora y laptop

1) Clases
    - Clase padre => Computadora
    - Clase hija => Laptop
2) Atributos:
    - Computadora: Ram, Marca, Procesador, Modelo, Almacenamiento
    - Laptop: Bateria, Peso, Pantalla, Tamaño
"""



class Computadora:
    # contructor
    def __init__(self, ram:int, marca:str, procesador:str, modelo:str, almacenamiento:str):
        self.ram = ram
        self.marca = marca
        self.procesador = procesador
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    # metodos
    def mostrar_info(self)->str:
        return (f"Computadora - Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Procesador: {self.procesador}, RAM: {self.ram}GB, "
                f"Almacenamiento: {self.almacenamiento}")
    
class Laptop(Computadora):
    # constructor
    def __init__(self,ram:int, marca:str, procesador:str, modelo:str, almacenamiento:str, bateria:str, peso:float, pantalla:float, tamanio:float):
        super().__init__(ram, marca, procesador, modelo, almacenamiento)
        self.bateria = bateria
        self.peso = peso
        self.pantalla = pantalla
        self.tamanio = tamanio
    
    def duracion_bateria(self)-> str:
        return f"La laptop tiene una duración de batería de {self.bateria} horas."
    
    def mostrar_info(self)->str:
        info = super().mostrar_info()
        return (f"{info}, Pantalla: {self.pantalla} pulgadas")
    
# crear instancias
computador_gamer = Computadora(16, "Asus", "Intel i7", "ROG Strix", "1TB SSD")
print(computador_gamer.mostrar_info())

laptop_empresa = Laptop(8, "Dell", "Intel i5", "Latitude", "512GB SSD", "10", 1.5, 14, 13.3)
print(laptop_empresa.duracion_bateria())
print(laptop_empresa.mostrar_info())


    
    


