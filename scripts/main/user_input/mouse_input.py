import pygame.mouse,math
import scripts.main.datas.map_datas as map_datas
import scripts.main.main_loop_functions.num_check as num_check

def get_tile_pos(mouse_pos,type):
    if type == "tile":
        return (mouse_pos[0] // (750 // 9), mouse_pos[1] // (750 // 9))


def tile_input():
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed(3)[0]:

        map_datas.all_tiles[get_tile_pos(pos,"tile")[0]][get_tile_pos(pos,"tile")[1]] = map_datas.current_num











