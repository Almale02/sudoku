import main_loop_functions.main_fc as funcs_main
import pygame
import user_input.mouse_input as mouse_input
import time


def main_looop(window,x_size,y_size):
    while True:
        for e in pygame.event.get():
            # quit handlering
            funcs_main.quit_handler(e)
            # num changeing
            funcs_main.num_changer(e)

        # grid drawing
        funcs_main.display_fcs(window,x_size,y_size)
        # tile input
        mouse_input.tile_input()
        # updating the screen
        pygame.display.update()

        # ups lock
        time.sleep(1 / 60)








