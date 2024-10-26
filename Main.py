import sys
import pygame
import time
import Button

clock = pygame.time.Clock()
pygame.font.init()
Width, Height = 330, 717
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("demo")

button1 = Button.Button("Sign In", 100, 400, 160, 60,)

def main() -> None:
    clock = pygame.time.Clock()
    run = True
    screen = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the close button is clicked
                run = False
                break
            if screen == 0:
                Window.fill('BLACK')
                mouse_pos = pygame.mouse.get_pos()
                if button1.is_hovered(mouse_pos):
                    button1.draw(Window, 'WHITE')
                else:
                    button1.draw(Window, (200, 200, 200))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.is_clicked(event):
                        screen = 1

            if screen == 1:
                Window.fill('WHITE')
        pygame.display.flip()  # Update the display with the drawn frame
        clock.tick(60)

if __name__ == "__main__":
    main()
