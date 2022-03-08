# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def camino():
    for i in range(0, 6):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
camino()

## VERSION 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def camino():
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
while not at_goal():
    camino()

### VERSION 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def camino():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
while not at_goal():
    if wall_in_front():
        camino()
    else:
        move()


### VERSION 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def camino():
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        move()
        while front_is_clear():
            move()
        turn_left()
        
while not at_goal():
    if wall_in_front():
        camino()
    else:
        move()

## MAZE

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()