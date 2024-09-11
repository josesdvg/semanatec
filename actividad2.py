from turtle import *
from random import randrange, choice
from freegames import square, vector

# Inicialización de la comida, la serpiente y su dirección
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores disponibles para la serpiente y la comida
colors = ['blue', 'yellow', 'purple', 'green', 'orange']

# Función para cambiar la dirección de la serpiente
def change(x, y):
    "Cambia la dirección de la serpiente."
    aim.x = x
    aim.y = y

# Función para verificar si la cabeza de la serpiente está dentro de los límites
def inside(head):
    "Devuelve True si la cabeza está dentro de los límites."
    return -200 < head.x < 190 and -200 < head.y < 190

# Función para generar colores aleatorios para la serpiente y la comida
def random_colors():
    "Genera colores aleatorios para la serpiente y la comida."
    snake_color = choice(colors)
    food_color = choice([color for color in colors if color != snake_color])
    return snake_color, food_color

# Función para mover la serpiente y actualizar la posición de la comida
def move():
    "Mueve la serpiente y actualiza la posición de la comida."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Si la serpiente choca, se dibuja en rojo
        update()
        return

    snake.append(head)

    if head == food:  # Si la serpiente come la comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # Cambiar colores cada vez que la serpiente coma la comida
        global snake_color, food_color
        snake_color, food_color = random_colors()
    else:
        snake.pop(0)

    # Movimiento aleatorio de la comida
    food_dir = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])
    new_food = food + food_dir
    if inside(new_food):  # Verificar si la nueva posición está dentro de los límites
        food.move(food_dir)

    clear()

    # Dibujar la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujar la comida
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)  # Ejecuta el movimiento cada 100ms

# Inicialización del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Controles de dirección
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Inicialización de colores al inicio del juego
snake_color, food_color = random_colors()

# Iniciar el movimiento de la serpiente
move()
done()
