import pygame
import scripts.main.datas.map_datas as map_datas
import sys
import scripts.display.display_fc.grid_draw as grid_draw

def quit_handler(e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def display_fcs(window,x_size,y_size):
    grid_draw.grid_draw(x_size,y_size,window)

def num_changer(e):
    if e.type == pygame.KEYDOWN:

        target_num = (57 - e.key - 9) * -1
        if target_num <= 9 or target_num >=1:
            map_datas.current_num = target_num -1
        print(target_num)

def fill_the_map(filler):
    for y in range(len(map_datas.all_tiles)):
        print("")
        for x in range(len(map_datas.all_tiles[y])):
            print(map_datas.all_tiles[x][y],end="")





