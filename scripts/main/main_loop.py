import main_loop_functions.main_fc as funcs_main
import pygame
import user_input.mouse_input as mouse_input
import time
import scripts.display.display_fc.draw_nums as draw_nums


def main_looop(window,x_size,y_size):
    funcs_main.fill_the_map("blank")

    while True:
        # get the mouse pos
        mouse_pos = pygame.mouse.get_pos()
        for e in pygame.event.get():
            # quit handlering
            funcs_main.quit_handler(e)
            # num changeing
            funcs_main.num_changer(e)


        # grid drawing
        funcs_main.display_fcs(window,x_size,y_size)
        # tile input
        mouse_input.tile_input()
        # drawing numbers3
        print(mouse_pos)
        draw_nums.draw_nums(window, mouse_pos)
        # updating the screen
        pygame.display.update()
        #clear the screen
        window.fill((0,100,100))
        # ups lock
        time.sleep(1 / 27)








