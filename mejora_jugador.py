from jugador import *
class Mejora():
    def __init__(self, aumentar_vida, aumentar_daño):
        self._aumentar_vida = aumentar_vida
        self._aumentar_daño = aumentar_daño

    #Definimos propertys y setters para poder utilizar los atributos privados de la clase.
    
    #Aumentar vida
    @property
    def aumentar_vida(self):
        return self._aumentar_vida
    @aumentar_vida.setter
    def aumentar_vida(self, vida):
        self._aumentar_vida = vida
    #Aumentar Daño
    @property
    def aumentar_daño(self):
        return self._aumentar_daño
    @aumentar_daño.setter
    def aumentar_daño(self, daño):
        self._aumentar_daño = daño   
        
        
    #Creamos la funcion que nos permitira subir el nivel del jugador       
    def SubeNivel(self, jugador):#Agregar la clase jugador
        jugador.vida += self.aumentar_vida
        jugador.daño += self.aumentar_daño
        jugador.nivel += 1
        print(f"{jugador.nombre} acaba de subir al nivel {jugador.nivel}")