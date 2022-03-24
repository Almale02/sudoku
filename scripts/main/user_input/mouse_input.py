import pygame.mouse
import scripts.main.datas.map_datas as map_datas

def get_tile_pos(mouse_pos,type):
    if type == "row":
        return mouse_pos[1] // (750 // 9)
    if type == "column":
        return mouse_pos[0] // (750 // 9)
    if type == "block":
        return  (mouse_pos[0] // (750 // 3), mouse_pos[1] // (750 // 3))
    if type == "tile":
        return (mouse_pos[0] // 9, mouse_pos[1] // 9)

def tile_input():
    pos = tuple()
    if pygame.mouse.get_pressed(3)[0]:
        pos = pygame.mouse.get_pos()
        print(pos)
        map_datas.blocks[get_tile_pos(pos,"block")[0]][get_tile_pos(pos,"block")[1]][get_tile_pos(pos,"tile")[0] % 3][get_tile_pos(pos,"tile")[1] % 3] = map_datas.current_num
        print(map_datas.blocks[get_tile_pos(pos,"block")[0]][get_tile_pos(pos,"block")[1]][get_tile_pos(pos,"tile")[0] % 3][get_tile_pos(pos,"tile")[1] % 3])








