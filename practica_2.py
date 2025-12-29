"""
Contexto: 🙌
Queremos modelar un animal con habilidades combinadas.
Consigna: ✍
Definí las siguientes clases:
    ● Volador: método moverse() imprime "Estoy volando"
    ● Nadador: método moverse() imprime "Estoy nadando"
    ● Pato: hereda de ambas clases, no sobrescribe moverse()
Paso a paso: ⚙
1.Creá un objeto Pato y llamá a moverse() (listo)
2. Usá Pato.__mro__ o help(Pato) para mostrar el orden de resolución
3. Cambiá el orden de herencia y volvé a probar
4. Agregá un método propio en Pato que combine ambos comportamientos
"""
class Volador:
    def moverse(self):
        print("Estoy volando")

class Nadador:
    def moverse(self):
        print("Estoy nadando")

class Pato(Volador, Nadador):
    def moverse(self):
        super().moverse()

    def moverse_combinado(self):
        print("Estoy volando y nadando")

class Ave(Nadador, Volador):
    def moverse(self):
        super().moverse()

    def moverse_combinado(self):
        print("Estoy volando y nadando")

# crear instancia de Pato
animal  = Pato()
animal.moverse()
animal.moverse_combinado()
print(Pato.__mro__)

# creo una nueva instancia con la clase nueva.
animal_2 = Ave()
animal_2.moverse()
animal_2.moverse_combinado()
print(Ave.__mro__)