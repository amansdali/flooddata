import sys
import pygame
import time

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, colour):
        pygame.draw.rect(screen, colour, self.rect, 0, 16)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, 'BLACK')
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

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
