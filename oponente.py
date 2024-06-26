import random

class Oponente:
    def __init__(self, nombre, vida, daño, golpes_acertados ,posicion):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.golpes_acertados = golpes_acertados
        self.posicion = posicion
        
    def posicion_oponente(self):
        posicion = random.choice(["izquierda", "centro", "derecha"])
        print(f"{self.nombre} se ha movido a la {posicion}.\n")
        return posicion
    
    def ataque_oponente(self):
        posicion = random.choice(["izquierda", "centro", "derecha"])
        print(f"{self.nombre} ataca a la posicion: {posicion}.\n")
        return posicion