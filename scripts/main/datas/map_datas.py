import pygame,os
from pathlib import Path

##C:\\Users\\gaspa\\Desktop\\Apps\\project\\pyton\\programok\\pythonProject\\assets\\1 - 9\\0.png"
_calls = 0
if _calls == 0:
    blocks = [[[[0 for w in range(3)] for q in range(3)] for x in range(3)] for y in range(3)]
    rows = [[0 for z in range(9)] for i in range(9)]
    column = [[0 for k in range(9)] for j in range(9)]
    all_tiles = [["blank" for i in range(9)] for x in range(9)]
    print(all_tiles[1][1])
    current_num = int()
    png_nums = []


    for i in range(9):
        i += 1
        png_nums.append(pygame.image.load("datas\\1 - 9\\"+ str(i) + ".png"))

    _calls += 1





