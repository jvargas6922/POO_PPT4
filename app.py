"""
Herencia en python

Metodo super(): permite llamar a un metodo de la clase padre desde una clase hija.
"""

class Persona:
    # Contructor de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo de la clase Persona
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Empleado(Persona):
    # Contructor de la clase Empleado
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    # Metodo de la clase Empleado(Exclusivo de la clase Empleado)
    def mostrar_salario(self):
        return f"Mi salario es {self.salario} dólares."
    
    # Sobrescribir el metodo saludar de la clase Persona
    def saludar(self):
        saludo_persona = super().saludar()
        return f"{saludo_persona} Soy un empleado y mi salario es {self.salario} dólares."
    
# Crear instancia de las clases
persona_1 = Persona("Ana", 28)
print(persona_1.saludar())

empleado_1 = Empleado("Joffred", 39, 1500)
print(empleado_1.mostrar_salario())
print(empleado_1.saludar())
