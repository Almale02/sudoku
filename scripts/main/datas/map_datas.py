import pygame,os
from pathlib import Path

##C:\\Users\\gaspa\\Desktop\\Apps\\project\\pyton\\programok\\pythonProject\\assets\\1 - 9\\0.png"
_calls = 0
if _calls == 0:
    all_tiles = [["blank" for i in range(9)] for x in range(9)]

    current_num = int()
    png_nums = []
    for i in range(9):
        i += 1
        png_nums.append(pygame.image.load("datas\\1 - 9\\"+ str(i) + ".png"))

    _calls += 1





