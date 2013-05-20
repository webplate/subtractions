#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform, os, pygame
from display_settings import *

def draw_sub(coord, n1, n2, result=''):
    x, y = coord
    #prepare numbers
    l1 = font.render(n1, True, txt_color) #texte, antialiasing, color
    l2 = font.render(n2, True, txt_color)
    l3 = font.render(result, True, txt_color)
    max_width = max(l1.get_width(), l2.get_width(), l3.get_width())
    max_len = max(len(n1), len(n2), len(result)) -1
    #prepare "decorations"
    bottom_line = font.render("_"*max_len, True, txt_color)
    sign = font.render("-", True, txt_color)
    #draw numbers
    gap = x + max_width
    display.blit(l1, (gap - l1.get_width(), y))
    display.blit(l2, (gap - l2.get_width(), y+txt_inter))
    display.blit(l3, (gap - l3.get_width(), y+2*txt_inter))
    #draw 'minus' and 'bottom line'
    display.blit(bottom_line, (gap - bottom_line.get_width(), y+txt_inter))
    display.blit(sign, (x, y+txt_inter))


#Set graphic driver according to platform
system = platform.system()
if system == 'Windows':    # tested with Windows 7
   os.environ['SDL_VIDEODRIVER'] = 'directx'
elif system == 'Darwin':   # tested with MacOS 10.5 and 10.6
   os.environ['SDL_VIDEODRIVER'] = 'Quartz'

#Initialize pygame
pygame.init()
if full_screen:
    display = pygame.display.set_mode(window_size, HWSURFACE | FULLSCREEN | DOUBLEBUF)
    pygame.mouse.set_visible(False)     #hide cursor
else:
    display = pygame.display.set_mode(window_size)

pygame.event.clear()        #clear event list to ignore previous pressures

font = pygame.font.Font(txt_font, txt_size) #name, size

#Main loop
frame = 0
t0 = pygame.time.get_ticks()
last_flip = t0
while True:
    display.fill(bg_color)
    draw_sub((100,300),"12345","5673"," 0045X")
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            #to check the refresh rate
            print float(pygame.time.get_ticks() - t0)/frame, "msec/frame"
            pygame.quit()
        elif event.type == KEYDOWN and event.key == switch_key :
            print 'down'
        elif event.type == pygame.MOUSEMOTION:
            coord = font.render(str(pygame.mouse.get_pos()), True, txt_color)
            display.blit(coord, pygame.mouse.get_pos())
    #flip every 16ms only (for smooth animation, particularly on linux)
    if pygame.time.get_ticks() > last_flip + 16 :
        last_flip = pygame.time.get_ticks()
        pygame.display.flip()
        frame += 1