
def leerJuegos(nombreArchivo: str) -> list:
    juego = {}
    juegos = []
    with open(nombreArchivo, "r") as file:
        for linea in file:
            game = (linea.strip().split(","))
            juego['nombre'] = game[0]
            juego['nJugadores'] = int(game[1])
            juego['precio'] = float(game[2])
            juego['consola'] = game[3]
            juego['anio'] = int(game[4])

            juegos.append(juego)
            juego = {}

    return juegos

def filtroPrecio(juegos: list) -> list:
    CANT_MAX_RESULTADOS = 10
    filtro = []
    precioMin = float(input("[+] Ingrese precio mínimo: "))
    precioMax = float(input("[+} Ingrese precio máximo: "))
    #precioMin = 5.0 #TODO: BORRAR
    #precioMax = 7.0 #TODO: BORRAR

    contador = 1
    for game in juegos:
        if contador <= CANT_MAX_RESULTADOS:
            if game["precio"] >= precioMin and game["precio"] <= precioMax:
                print(contador,   game) #TODO: BORRAR
                filtro.append(game)
                contador += 1
    return filtro

def filtroJugador(juegos: list) -> list:
    CANT_MAX_RESULTADOS = 10
    filtro = []
    esSinglePlayer = input("[+] Singleplayer o Multiplayer (s/n): ").lower()

    if esSinglePlayer == "s":
        contador = 1
        for game in juegos:
            if contador <= CANT_MAX_RESULTADOS:
                if game["nJugadores"] == 1:
                    #print(contador,   game) #TODO: BORRAR
                    filtro.append(game)
                    contador += 1
        return filtro
    else:
        contador = 1
        for game in juegos:
            if contador <= CANT_MAX_RESULTADOS:
                if game["nJugadores"] > 1:
                    #print(contador,   game) #TODO: BORRAR
                    filtro.append(game)
                    contador += 1
        return filtro
    
def filtroConsolaAnio(juegos: list) -> list:
    CANT_MAX_RESULTADOS = 10
    filtro = []
    consola = input("[+] Ingrese nombre de consola: ")
    anio = int(input("[+] Ingrese año: "))

    contador = 1
    for game in juegos:
        if contador <= CANT_MAX_RESULTADOS:
            if game["consola"] == consola and game["anio"] == anio:
                #print(contador,   game) #TODO: BORRAR
                filtro.append(game)
                contador += 1
    return filtro

def escribirArchivo(juegos: list):
    nombreArchivo = "filtro_juegos.txt"
    filtro = []
    while True:
        print("***MENÚ ESCRITURA***\n1. Escribir filtro jugador\n2. Escribir filtro precio\n3. Escribir filtro consola y año\n")
        op = input("[+] Ingrese opción: ")
        op = int(op)
        if op == 1:
            filtro = juegos[op - 1]
            break
        elif op == 2:
            filtro = juegos[op - 1]
            break
        elif op == 3:
            filtro = juegos[op - 1]
            break
        else:
            print("[!] ERROR: Ingrese un valor válido")

    if len(filtro) != 0:
        with open(nombreArchivo, "w") as file:
            for d in filtro:
                texto = list(d.values())
                file.write(texto + "\n")
        print("[!] Archivo creado!!")
    else:
        print("[!] No hay infomación para escribir")

def menu():
    LISTA_JUEGOS = leerJuegos("juegos.csv")
    filtro1_juegos = []
    filtro2_juegos = []
    filtro3_juegos = []
    isRunnig = True

    while isRunnig:
        MENU = "****MENU PRINCIPAL****\n1. Filtro Jugador\n2. Filtro precio\n3. Filtro consola y año\n4. Escribir archivo\n5. Salir\n"
        print(MENU)
        op = input("[+] Ingrese una opción: ")

        if op == "1":
            print("FILTRO JUGADOR")
            filtro1_juegos = filtroJugador(LISTA_JUEGOS)
            print("[!] El resultado de la búsqueda es (Los 10 primeros)")
            for j in filtro1_juegos:
                print(list(j.values()))
        elif op == "2":
            print("FILTRO PRECIO")
            filtro2_juegos = filtroPrecio(LISTA_JUEGOS)
            if len(filtro2_juegos) != 0:
                print("[!] El resultado de la búsqueda es (Los 10 primeros)")
                for j in filtro2_juegos:
                    print(list(j.values().sort()))
            else:
                print("[!] No hay juegos en ese rango de precios")
        elif op == "3":
            print("FILTRO CONSOLA Y AÑO")
            filtro3_juegos = filtroConsolaAnio(LISTA_JUEGOS)

            if len(filtro3_juegos) != 0:
                print("[!] El resultado de la búsqueda es (Los 10 primeros)")
                for j in filtro3_juegos:
                    print(list(j.values()))
            else:
                print("[!] No hay información que escribir")
        elif op == "4":
            print("ESCRIBIR ARCHIVO")
            filtroEscribir = []
            filtroEscribir.append(filtro1_juegos)
            filtroEscribir.append(filtro2_juegos)
            filtroEscribir.append(filtro3_juegos)
            escribirArchivo(filtroEscribir)
        elif op == "5":
            print("[!] Saliendo del sistema...")
            isRunnig = False
        else:
            print("[!] Opción ingresada no es válida")

if __name__ == "__main__":
    menu()