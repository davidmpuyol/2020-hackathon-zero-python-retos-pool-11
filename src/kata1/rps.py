from random import randint, choice

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if player == 'piedra':
        if ai == 'papel':
            return 'Perdiste!'
        elif ai == 'piedra':
            return 'Empate!'
        elif ai == 'tijeras':
            return 'Ganaste!'
    elif player == 'papel':
        if ai == 'papel':
            return 'Empate!'
        elif ai == 'piedra':
            return 'Ganaste!'
        elif ai == 'tijeras':
            return 'Perdiste!'
    elif player == 'tijeras':
        if ai == 'papel':
            return 'Ganaste!'
        elif ai == 'piedra':
            return 'Perdiste!'
        elif ai == 'tijeras':
            return 'Empate!'

# Entry Point
def Game():
    eleccion = ""
    while not 0 <= eleccion <= 2:
        print("Piedra Papel Tijeras")
        print("0 - Piedra")
        print("1 - Papel")
        print("2 - Tijeras")
        eleccion = int(input("Elige tu tirada:"))
    player = options[eleccion]
    ai = choice(options)
    winner = quienGana(player, ai)
    print(winner)