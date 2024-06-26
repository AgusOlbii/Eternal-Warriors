from datos import *


#SELECCIONAR UN JUGADOR
def seleccionar_jugador():
    while True:
        cont = 0
        print(f"Selecciona un jugador (1, 2, 3, 4, 5 o 6)\n")
        #MOSTRANDO JUGADORES
        for jugador in jugadores:
            cont += 1
            print(f"jugador {cont}: \n")
            print(f"{jugador}\n")
        #SELECCIONANDO JUGADOR
        while True:
            jugador_seleccionado = int(input("Seleccione el jugador que mas le guste!"))
            if jugador_seleccionado > 6 or jugador_seleccionado < 1:
                print("El jugador seleccionado es incorrecto. Intentelo nuevamente.\n")
            else:
                jugador_seleccionado = jugador_seleccionado - 1
                break
        print(f"Usted escogio al jugador: {jugadores[jugador_seleccionado].nombre}\n")
        return jugador_seleccionado
        

#SUBIR DE NIVEL
def subida_nivel(jugador_seleccionado):
    while True:
        subir_nivel.SubeNivel(jugadores[jugador_seleccionado])
        break
        
#Inicializamos la partida!!!!
def empezar_partida(jugador_seleccionado):
    jugador = jugadores[jugador_seleccionado]
    jugador.vida = 100
    oponente.vida = 100
    while True:
        print(f"Jugador {jugador.nombre} tiene {jugador.vida}% de vida\n Oponente {oponente.nombre} tiene {oponente.vida}% de vida\n")
        #Se llaman a las funciones dentro de las clases Jugador y Oponente para saber la posicion del jugador y hacia donde ataca el oponente.
        ataque_jugador = jugador.posicion_ataque_jugador()
        posicion_oponente = oponente.posicion_oponente()
        #Se condiciona si el jugador acerto el golpe o no
        if ataque_jugador == posicion_oponente:
            print(f"{jugador.nombre} ha acertado el golpe!\n")
            oponente.vida -= jugador.daño
            jugador.golpes_acertados += 1
        else:
            print(f"{jugador.nombre} ha fallado el golpe!\n")
        #Se llaman a las funciones dentro de las clases Jugador y Oponente para saber la posicion del jugador y hacia donde ataca el oponente.
        posicion_jugador = jugador.mover_jugador()
        ataque_oponente = oponente.ataque_oponente()
        #Se condicion si el oponente acerto el golpe
        if ataque_oponente == posicion_jugador:
            print(f"{oponente.nombre} ha acertado el golpe!\n")
            jugador.vida -= oponente.daño
        else:
            print(f"{oponente.nombre} ha fallado el golpe!\n")
        if jugador.vida <= 0:
            print("Ha perdido la partida! Intentalo de nuevo con el mismo personaje o selecciona uno distinto!!\n")
            break
        elif oponente.vida <= 0:
            print("Acaba de derrotar al oponente!!\n")
            break
    if jugador.golpes_acertados >= 3:
        subida_nivel(jugador_seleccionado)

#Funcion para mostrar las caracteristicas del personaje seleccionado
def caracteristicas_personajes(jugador_seleccionado):
        print(f"jugador: \n")
        print(f"{jugadores[jugador_seleccionado]}\n")
        

#CREAMOS EL MENU PRINCIPAL!      
def menu():
    jugador_seleccionado = None
    while True:
        print("------------Eternal Warriors------------")
        print("////////////////////////////////////////")
        print(f"Seleccione una opcion!\n1-Seleccionar un jugador\n2-Caracteristicas del personaje\n3-Comenzar partida\n4-Salir\n")
        opc = int(input(""))
        if opc == 1:
            jugador_seleccionado = seleccionar_jugador()
        elif opc == 2:
            if jugador_seleccionado != None:
                caracteristicas_personajes(jugador_seleccionado)
            else:
                print("Seleccione un personaje para poder ver sus caracteristicas!\n")
                #subida_nivel(jugador_seleccionado)
        elif opc == 3:
            if jugador_seleccionado != None:
                empezar_partida(jugador_seleccionado)
            else:
                print("Seleccione un personaje para comenzar a jugar!\n")
        elif opc == 4:
            print("Gracias por jugar Eternal Warriors! Nos vemos pronto guerrero!!\n")
            break
        else:
            print("Acaba de escoger una opcion invalida, intentelo de nuveo!\n")
     
menu()