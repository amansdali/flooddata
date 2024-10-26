import sys
import pygame
import time

class RoundButton:
    def __init__(self, img1, img2, x, y, width, height):
        self.img1 = pygame.image.load(img1)
        self.img2 = pygame.image.load(img2)
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

    def draw(self, screen, hovered):
        if hovered:
            screen.blit(self.img1, (self.x,self.y))
        else:
            screen.blit(self.img2, (self.x, self.y))

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False

    def is_hovered(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
