"""
Herencia multiple en Python
"""
# Clase padre 1
class Volador:
    def volar(self):
        return "Estoy volando"
    
# Clase padre 2
class Nadador:
    def nadar(self):
        return "Estoy nadando"


class Pato(Volador, Nadador):
    def quack(self):
        return "Cuac cuac"


# Crear una instancia de Pato
pato = Pato()
print(pato.volar())  # Llamada al método de Volador
print(pato.nadar())  # Llamada al método de Nadador
print(pato.quack())  # Llamada al método de Pato