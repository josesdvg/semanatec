from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Función para manejar el clic en la pantalla y lanzar la bola
def tap(x, y):
    "Responde al toque de pantalla."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10  # Aumentar la velocidad del proyectil
        speed.y = (y + 200) / 10  # Aumentar la velocidad del proyectil

# Función para verificar si un objeto está dentro de la pantalla
def inside(xy):
    "Devuelve True si el objeto está dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Función para dibujar la bola y los objetivos
def draw():
    "Dibuja la bola y los objetivos."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  # Dibuja los objetivos como puntos azules

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Dibuja la bola como un punto rojo

    update()

# Función para mover la bola y los objetivos
def move():
    "Mueve la bola y los objetivos."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2  # Aumentar la velocidad de los balones

    if inside(ball):
        speed.y -= 0.7  # Aumentar la gravedad para el proyectil
        ball.move(speed)

    # Crear una copia de los objetivos y limpiarlos
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Reposicionar los balones cuando salgan de la ventana
    for target in targets:
        if not inside(target):
            target.x = 200  # Reposiciona el balón al borde derecho de la pantalla

    ontimer(move, 25)  # Aumentar la frecuencia del movimiento

# Configuración inicial del juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
