def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_steps(steps):
    for i in range(steps):
        move()

i = 0 
while i < 4:
    move_steps(3)
    turn_left()
    move_steps(3)
    
    if i < 3:
        turn_right()
        move()
        turn_right()
        
    i = i + 1
