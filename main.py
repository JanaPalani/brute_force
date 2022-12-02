import pygame 
pygame.init()
import time 
plot = pygame.display.set_mode((500,500))

x_axis = 20
y_axis = 20
box_value = {}

start_box =(0,0)
box_value[start_box] = 'v'

end_box =(x_axis-1,y_axis-1)
box_value[end_box] = 'v'

for y in range(y_axis):
    for x in range(x_axis):
        box_value[(x,y)] = 0

obstacle_drop = False
obstacles  = []

def back_move():
    global stack,pos
    stack = stack[:-1]
    pos = stack[-1]
    
stack = []

neighbours = [(0,-1),(-1,0),(0,1),(1,0)]
pos = start_box
move = False

def move_maze():
    global stack,pos,move
    if pos not in stack:
        stack.append(pos)
    else:
        pass
    box_value[pos] = 'visited'

    for i in neighbours:
        posi = (pos[0]+i[0],pos[1]+i[1])
        if  posi[0] <  0 or posi[0] > 19 or  posi[1] < 0 or  posi[1] > 19:
            continue
            
        else:
            if box_value[posi] == 'visited' or  box_value[posi] == 1:
                continue 
            else:
                if posi == end_box:
                    move = False
                pos = posi
                break
    else:
        back_move()
 
run = True
clock = pygame.time.Clock()

while run :
    clock.tick(60)
    plot.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type  == pygame.MOUSEBUTTONDOWN:
            obstacle_drop = True
        if event.type == pygame.MOUSEBUTTONUP:
            obstacle_drop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move = True 

    for i in box_value.keys():
        pygame.draw.rect(plot,(255,255,255),pygame.Rect(25*i[0],25*i[1],25,25),2)

    pygame.draw.rect(plot,(0,100,0),pygame.Rect(25*start_box[0],25*start_box[1],25,25))
    pygame.draw.rect(plot,(150,0,0),pygame.Rect(25*end_box[0],25*end_box[1],25,25))

    if obstacle_drop:
        position  = pygame.mouse.get_pos()
        position = (position[0]//25,position[1]//25)
        if (position == (0,0)) or (position == (19,19)):
            pass
        else:
            if position not in obstacles :
                box_value[position] = 1
                obstacles.append(position)
    
    for obs in obstacles:
        pygame.draw.rect(plot,(255,255,255),pygame.Rect(25*obs[0],25*obs[1],25,25))
    
    for each_move in stack:
            pygame.draw.rect(plot,(0,255,255),pygame.Rect(25*each_move[0],25*each_move[1],25,25))
    
    if move:
        move_maze()
        
    pygame.display.flip()
