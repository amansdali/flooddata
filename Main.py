import sys
import pygame
import time
import Button
import InputBox
import datetime
import RoundButton
import geocoder

clock = pygame.time.Clock()
pygame.font.init()
Width, Height = 370, 717
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("demo")

button0 = RoundButton.RoundButton('roundButton3.png', 'roundButton4.png', 10, 10, 47, 41)
button1 = Button.Button("Sign In", 100, 300, 160, 60,)
button2 = Button.Button("Sign Up", 100, 400, 160, 60,)
button3 = RoundButton.RoundButton('roundButton1.png', 'roundButton2.png', 50, 150, 275, 277)
button4 = Button.Button("Database", 100, 480, 160, 60,)

FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.SysFont("arial", 15)
txt1 = FONT.render("Flood Feedback", True, "white")
txt2 = FONT2.render('Enter Flood Duration', True, "black")

def main() -> None:
    clock = pygame.time.Clock()
    run = True
    screen = 0
    duration = ''
    durationin = InputBox.InputBox(duration, 40, 220, 280, 25)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the close button is clicked
                run = False
                break
            mouse_pos = pygame.mouse.get_pos()
            if screen == 0:
                Window.fill((25,25,112))
                Window.blit(txt1, (80, 150))
                if button1.is_hovered(mouse_pos):
                    button1.draw(Window, (220, 220, 220))
                else:
                    button1.draw(Window, 'WHITE')
                if button2.is_hovered(mouse_pos):
                    button2.draw(Window, (220, 220, 220))
                else:
                    button2.draw(Window, 'WHITE')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.is_clicked(event):
                        screen = 1
                    elif button2.is_clicked(event):
                        screen = 2

            elif screen == 1:
                Window.fill('WHITE')
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 0
                screen = 3

            elif screen == 2:
                Window.fill('WHITE')
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 0
                screen = 3

            elif screen == 3:
                Window.fill('WHITE')
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if button3.is_hovered(mouse_pos):
                    button3.draw(Window, True)
                else:
                    button3.draw(Window, False)
                if button4.is_hovered(mouse_pos):
                    button4.draw(Window, (255, 213, 128))
                else:
                    button4.draw(Window, (244, 187, 68))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 0
                    elif button3.is_clicked(event):
                        screen = 4
                    elif button4.is_clicked(event):
                        screen = 5

            elif screen == 4:
                Window.fill((255, 213, 128))
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 3
                    elif durationin.is_clicked(event):
                        durationin.isselected = True
                elif event.type == pygame.KEYDOWN:
                    if durationin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            duration = duration[0:-1]
                        else:
                            duration += event.unicode
                ip = geocoder.ip("me")
                latlng = str(ip.latlng)



                latlngtxt = FONT2.render('Latitue, Longitude: '+latlng, True, "black")

                Window.blit(latlngtxt, (40, 120))
                Window.blit(txt2, (40, 190))
                durationin.draw(Window, duration)

            elif screen == 5:
                Window.fill('WHITE')

        pygame.display.flip()  # Update the display with the drawn frame
        clock.tick(60)

if __name__ == "__main__":
    main()
