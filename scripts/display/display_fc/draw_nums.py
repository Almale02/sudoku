import scripts.main.datas.map_datas as map_datas
import scripts.main.user_input.mouse_input as mouse_input
import pygame
def draw_nums(window,pos):
    for y in range(len(map_datas.all_tiles)):
        for x in range(len(map_datas.all_tiles[y])):
            if not map_datas.all_tiles[x][y] == "blank":
                window.blit(map_datas.png_nums[map_datas.all_tiles[x][y]],(x * 83.3, y * 83.3))

