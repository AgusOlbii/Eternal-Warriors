class Jugador:
    def __init__(self, nombre, nivel, vida, daño, golpes_acertados, posicion):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.daño = daño
        self.golpes_acertados = golpes_acertados
        self.posicion = posicion
        
     #Mostramos los estadisticas del jugador
    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel: {self.nivel}\nVida: {self.vida}\nDaño: {self.daño}\nGolpes Acertados: {self.golpes_acertados}"
    
    #Funcion para poder mover nuestro player
    def mover_jugador(self):
        nueva_posicion = input("Ingrese la posicion a la que desea colocarse (izquierda, centro, derecha): ")
        if nueva_posicion in ["izquierda", "centro", "derecha"]:
            self.posicion = nueva_posicion 
            print(f"{self.nombre} se ha movido a la {nueva_posicion}")
            return nueva_posicion
        else:
            print("Posicion invalida, no se movio")
            
    #Funcion para elegir posicion de ataque de nuestro jugador
    def posicion_ataque_jugador(self):
        while True:
            ataque_jugador = str(input("Ingrese la posicion de ataque (izquierda, centro, derecha): "))
            if ataque_jugador != "izquierda" and ataque_jugador != "centro" and ataque_jugador != "derecha":
                print("Ingrese una posicion valida.")
            else:
                return ataque_jugador