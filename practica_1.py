"""
Contexto: 🙌
Vas a diseñar un sistema para representar diferentes tipos de medios de transporte.
Consigna: ✍
Implementá las siguientes clases en Python usando
herencia:
- Vehiculo (clase base): marca, modelo, moverse()
- Auto (subclase): sobrescribe moverse() con "Conduciendo por la carretera"
- Bicicleta (subclase): sobrescribe moverse() con "Pedaleando"
- Motocicleta (subclase): agrega atributo cilindrada

Paso a paso: ⚙
1. Aplicar herencia simple (listo)
2. Usar sobrescritura de métodos (listo)
3. Probar comportamiento polimórfico con un bucle que recorra una lista de vehículos y llame a moverse()
"""

# clase base(Padre)
class Vehiculo:
    # constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # metodo
    def moverse(self):
        pass

# Sub-clase
class Auto(Vehiculo):
    def moverse(self):
        return "Conduciendo por la carretera"
    
# Sub-clase  
class Bicicleta(Vehiculo):
    def moverse(self):
        return "Pedaleando"
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def moverse(self):
        return "Conduciendo la motocicleta"
    

# lista de vehiculos
vehiculos = [
        Auto("Toyota", "Corolla"),
        Bicicleta("Giant", "Escape 3"),
        Motocicleta("Yamaha", "MT-07", 689)
    ]

# recorrer mi lista en un bucle.
for vehiculo in vehiculos:
    print(f"{vehiculo.marca} {vehiculo.modelo}: {vehiculo.moverse()}")