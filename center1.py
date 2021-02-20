count = 0
middle = 0
while not wall_in_front():
    move()
    count = count + 1
        
middle = (int(count / 2))
turn_left()
turn_left()

i = 0
while i < middle:
    move()
    i = i + 1
    
put()
