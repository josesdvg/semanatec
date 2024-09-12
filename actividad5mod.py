from random import shuffle
from turtle import *
from freegames import path
import time

# cargar foto del coche 
car = path('car.gif')

# simbolos unicos 32, cada uno se repite
symbols = ['🍎', '🍌', '🍇', '🍓', '🍒', '🍉', '🍍', '🍑',
           '🥝', '🥥', '🥭', '🍋', '🍊', '🍈', '🍐', '🍏',
           '🥑', '🍔', '🍕', '🍗', '🍖', '🍤', '🍟', '🍪',
           '🍰', '🍦', '🍧', '🍩', '🍫', '🍬', '🍭', '🍮'] * 2

state = {'mark': None}
hide = [True] * 64
taps = 0  # contador de taps
showing_fruits = True  # estado inicial para aneseñar todasls frutas 

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    if -200 <= x < 200 and -200 <= y < 200:
        return int((x + 200) // 50 + ((y + 200) // 50) * 8)
    return None

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps, showing_fruits

    # ignorar taps cuando se estan enseñando las frutas 
    if showing_fruits:
        return

    spot = index(x, y)
    if spot is None or spot < 0 or spot >= 64:
        return  # ingorar taps fuera del luegar

    mark = state['mark']
    taps += 1  # incrementa tap count
    print(f"Tap registered at index {spot}, number of taps: {taps}")

    # update la visibilidad de tiles
    if mark is None or mark == spot or symbols[mark] != symbols[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # enseñar el tile que se toca y comparar 
    draw_tile(spot)
    if mark is not None:
        draw_tile(mark)

    # ver que todos esten revelados 
    if all(not hidden for hidden in hide):
        print("Congratulations! All tiles are revealed.")

def show_all_fruits():
    "Reveal all fruits for a short period at the start."
    global showing_fruits

    #enseña frutas 3 segundos  
    showing_fruits = True
    draw()  
    time.sleep(3)

    # esconder emojis y empezar
    for i in range(64):
        hide[i] = True
    showing_fruits = False
    draw()  #re escribir el board 

def draw_tile(count):
    "Draw a specific tile (with or without the symbol)."
    x, y = xy(count)

    if hide[count]:
        square(x, y) 
        up()
        goto(x + 15, y + 5) 
        color('black')
        write(symbols[count], align="center", font=('Arial', 30, 'normal'))
    update()  

def draw():
    "Draw the car image and the game board."
    clear()  

   
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        draw_tile(count)

    update()  

shuffle(symbols)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)

show_all_fruits()
onscreenclick(tap)
done()
