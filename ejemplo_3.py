"""
¿En qué consistirá la Demo?
Vas a implementar una clase base con un método común, y dos subclases que sobrescriben ese método de
forma distinta.
🔹 Clase base Animal:
    ● Atributo: nombre (listo)
    ● Método: emitir_sonido() que imprima "Sonido genérico"
🔹 Subclases Perro y Gato:
    ● Sobrescriben emitir_sonido() para imprimir:
        ○ "Guau!" en Perro
        ○ "Miau!" en Gato
🔹 Qué se debe probar:
    ● Crear un objeto de cada subclase
    ● Llamar a emitir_sonido() desde cada uno
    ● Verificar que el comportamiento es distinto, aunque el método se llama igual
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def creacion(self):
        print(f"Se ha creado un perro llamado {self.nombre}")

    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau!")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau!")
    
    def creacion(self):
        print(f"Se ha creado un gato llamado {self.nombre}")

# pruebas 
mi_perro = Perro("Firulais")
mi_perro.creacion()
mi_perro.emitir_sonido()
print("-----" * 10)
mi_gato = Gato("Misu")
mi_gato.creacion()
mi_gato.emitir_sonido()