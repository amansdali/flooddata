import pygame

class InputBox:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.textrect = pygame.Rect(x+5, y+5, width, height)
        self.isselected = False

    def draw(self, screen, text):
        if self.isselected:
            pygame.draw.rect(screen, 'WHITE', self.rect, 0, 16)
        else:
            pygame.draw.rect(screen, (240,240,240), self.rect, 0, 16)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(text, True, 'BLACK')
        screen.blit(text_surface, self.textrect)

    def is_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False
