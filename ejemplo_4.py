"""
¿En qué consistirá la Demo?
Vas a crear una clase Pato que herede métodos de dos clases distintas, y observarás cómo Python decide cuál
método usar si hay conflicto.
🔹 Clase Volador:
    ● Método: moverse() imprime "El pato vuela"
🔹 Clase Nadador:
    ● Método: moverse() imprime "El pato nada"
🔹 Clase Pato:
    ● Hereda de ambas: class Pato(Volador, Nadador)
    ● No implementa moverse()
🔹 Qué se debe probar:
    1. Crear un objeto Pato
    2. Llamar a moverse()
    3. Usar Pato.__mro__ o help(Pato) para inspeccionar el orden de búsqueda
    4. Cambiar el orden de herencia (class Pato(Nadador, Volador)) y repetir)
"""

class Volador:
    def moverse(self):
        return f"El pato vuela"


class Nadador:
    def moverse(self):
        return f"El pato nada"
    
class Pato(Volador, Nadador):
    pass 
    # La clase Pato no implementa ningun metodo en este caso.

class Duck(Nadador, Volador):
    pass
    # La clase Duck no implementa ningun metodo en este caso.

pato_1 = Pato()
print(pato_1.moverse())  # Llamada al método moverse()
print(Pato.__mro__)  # Inspeccionar el orden de búsqueda de métodos
# print(help(Pato))  # Inspeccionar el orden de búsqueda de métodos

pato_2 = Duck()
print(pato_2.moverse())  # Llamada al método moverse()  # Inspeccionar el orden de búsqueda de métodos
print(Duck.__mro__)