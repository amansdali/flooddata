import sys
import pygame
import time
clock = pygame.time.Clock()
pygame.font.init()
Width, Height = 1320, 2868
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("demo")

def main():
    clock = pygame.time.Clock()
    run = True
    screen = 0
    while run:
        for event in pygame.event.get():
        if screen == 0:
            Window.fill('BLACK')
        if screen == 1:


if __name__ == "__main__":
    main()
