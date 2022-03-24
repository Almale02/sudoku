import pygame

def grid_draw(x_size,y_size,surface):
    # vertical lines
    for i in range(9):
        i += 1
        next_pos_x = i * x_size / 9
        if i  % 3 == 0:
            pygame.draw.line(surface,(255,255,255),(next_pos_x,0),(next_pos_x,y_size))
        else:
            pygame.draw.line(surface, (100, 100, 100), (next_pos_x, 0), (next_pos_x, y_size))
    # horizontal lines
    for i in range(9):
        i += 1
        next_pos_y = i * x_size / 9
        if i % 3 == 0:
            pygame.draw.line(surface,(255,255,255),(0,next_pos_y),(x_size,next_pos_y))
        else:
            pygame.draw.line(surface, (100, 100, 100),(0, next_pos_y), (x_size,next_pos_y))


