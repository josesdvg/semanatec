from random import choice
from turtle import *
from freegames import floor, vector

# Estado inicial del juego y objetos de Turtle
state = {'score': 0}  # Puntuación del jugador
path = Turtle(visible=False)  # Turtle para dibujar el laberinto
writer = Turtle(visible=False)  # Turtle para mostrar la puntuación
aim = vector(5, 0)  # Dirección inicial de Pac-Man
pacman = vector(-40, -80)  # Posición inicial de Pac-Man
ghosts = [  # Posiciones y direcciones iniciales de los fantasmas
    [vector(-180, 160), vector(20, 0)],
    [vector(-180, -160), vector(0, 20)],
    [vector(100, 160), vector(0, -20)],
    [vector(100, -160), vector(-20, 0)],
]

# Mapa del juego, donde 1 es un espacio con puntos y 0 es una pared
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Dibuja un cuadrado en la posición (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):  # Dibuja un cuadrado con 4 lados
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Devuelve el índice del mapa correspondiente al punto actual."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)  # Convierte las coordenadas en un índice de la lista de tiles
    return index

def valid(point):
    "Verifica si el punto es válido dentro del mapa (si no es una pared)."
    index = offset(point)

    if tiles[index] == 0:  # Si el punto es una pared, no es válido
        return False

    index = offset(point + 19)  # Verifica el punto un poco más allá para evitar errores de colisión

    if tiles[index] == 0:  # Si el punto es una pared, no es válido
        return False

    return point.x % 20 == 0 or point.y % 20 == 0  # Asegura que se mueve en pasos de 20 unidades

def world():
    "Dibuja el laberinto basado en los datos de tiles."
    bgcolor('black')  # Fondo negro
    path.color('blue')  # Color de las paredes

    for index in range(len(tiles)):  # Recorre todos los elementos de tiles
        tile = tiles[index]

        if tile > 0:  # Si es un espacio (no una pared)
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)  # Dibuja un cuadrado en esa posición

            if tile == 1:  # Si hay un punto comestible
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')  # Dibuja el punto comestible

def move():
    "Mueve a Pac-Man y a todos los fantasmas."
    writer.undo()
    writer.write(state['score'])  # Actualiza la puntuación

    clear()  # Borra el dibujo anterior

    if valid(pacman + aim):  # Verifica si Pac-Man puede moverse en la dirección actual
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:  # Si Pac-Man come un punto
        tiles[index] = 2  # Marca el punto como comido
        state['score'] += 1  # Incrementa la puntuación
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)  # Borra el punto comido

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # Dibuja a Pac-Man

    for point, course in ghosts:  # Mueve a cada fantasma
        # Calcula la distancia entre el fantasma y Pac-Man
        options = []
        if pacman.x > point.x and valid(point + vector(5, 0)):  # Si Pac-Man está a la derecha
            options.append(vector(5, 0))
        elif pacman.x < point.x and valid(point + vector(-5, 0)):  # Si Pac-Man está a la izquierda
            options.append(vector(-5, 0))

        if pacman.y > point.y and valid(point + vector(0, 5)):  # Si Pac-Man está arriba
            options.append(vector(0, 5))
        elif pacman.y < point.y and valid(point + vector(0, -5)):  # Si Pac-Man está abajo
            options.append(vector(0, -5))

        # Si hay opciones válidas para moverse hacia Pac-Man, elige una
        if options:
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y
        else:
            # Si no hay movimientos válidos hacia Pac-Man, sigue moviéndose en la dirección actual o elige otra aleatoria
            if not valid(point + course):
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice([option for option in options if valid(point + option)])
                course.x = plan.x
                course.y = plan.y

        # Mueve el fantasma en la dirección calculada
        point.move(course)

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')  # Dibuja al fantasma

    update()

    # Verifica si algún fantasma ha atrapado a Pac-Man
    for point, course in ghosts:
        if abs(pacman - point) < 20:  # Si la distancia es menor a 20, el juego termina
            return

    ontimer(move, 100)  # Llama a la función move nuevamente después de 100 ms

def change(x, y):
    "Cambia la dirección de Pac-Man si es válida."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Configuración inicial de la ventana y control del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')  # Cambia la dirección de Pac-Man a la derecha
onkey(lambda: change(-5, 0), 'Left')  # Cambia la dirección de Pac-Man a la izquierda
onkey(lambda: change(0, 5), 'Up')  # Cambia la dirección de Pac-Man hacia arriba
onkey(lambda: change(0, -5), 'Down')  # Cambia la dirección de Pac-Man hacia abajo
world()  # Dibuja el mundo
move()  # Comienza el movimiento
done()  # Finaliza el programa
