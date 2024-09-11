from turtle import *
import turtle
from freegames import vector
#oara cambiar de color debe ser la mayúscula y forma minuscula
#fucnion para dibujar línea
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    color(current_color)  # Aplicar color
    goto(end.x, end.y)

#funcion para dibujar cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    color(current_color)  # Aplicar color
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función para dibujar un círculo 
def circle(start, end):
    "Draw circle from start to end using the radius defined by the distance from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    color(current_color)  # Aplicar color
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5  # Calcula el radio usando la distancia
    turtle.circle(radius)
    end_fill()

#funcion para dibujar un rectángulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    color(current_color)  # Aplicar color
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

#funcion para dibujar un triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    color(current_color)  # Aplicar color
    for _ in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

# funcion para manejar los clics 
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#función para guardar configuracion del estado actual
def store(key, value):
    "Store value in state at key."
    state[key] = value

# Función para cambiar el color globalmente
def change_color(new_color):
    global current_color
    current_color = new_color

# configuracion inicial del juego
state = {'start': None, 'shape': line}
current_color = 'black'  # Color inicial
setup(420, 420, 370, 0)

#asignamos los evenots de clic en la pantalla y de picar teclas
onscreenclick(tap)
listen()
onkey(undo, 'u')

#ponemos los colores disponibles con el amarillo agregado para cambiar de color debe ser mayúscula
onkey(lambda: change_color('black'), 'K')  # Negro
onkey(lambda: change_color('white'), 'W')  # Blanco
onkey(lambda: change_color('green'), 'G')  # Verde
onkey(lambda: change_color('blue'), 'B')   # Azul
onkey(lambda: change_color('red'), 'R')    # Rojo
onkey(lambda: change_color('yellow'), 'Y') # Amarillo

#agregamos las opciones de circulo y rectangulo y triangulo 
onkey(lambda: store('shape', line), 'l')        # Línea
onkey(lambda: store('shape', square), 's')      # Cuadrado
onkey(lambda: store('shape', circle), 'c')      # Círculo
onkey(lambda: store('shape', rectangle), 'r')   # Rectángulo
onkey(lambda: store('shape', triangle), 't')    # Triángulo

done()
