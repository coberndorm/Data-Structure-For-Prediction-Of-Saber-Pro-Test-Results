
def torresDeHanoi (altura, origen, intermedio, destino):
    if (altura < 0):
        print("No hay discos")
    if (altura == 1):
        print("Disco " + str (altura) + " desde " + str (origen) + " hacia " + str (destino))
    if (altura>1):
        torresDeHanoi(altura-1, origen, destino,intermedio)
        print("Disco " + str (altura) + " desde " + str (origen) + " hacia " + str (destino))
        torresDeHanoi(altura-1, intermedio, origen,destino)

torresDeHanoi(3, 0,1,2)

