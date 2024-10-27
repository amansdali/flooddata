import pygame
import Button
import InputBox
import datetime
import RoundButton
import geocoder

# Setup
clock = pygame.time.Clock()
pygame.font.init()
Width, Height = 370, 717
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("demo")
START, SIGNIN, SIGNUP, MENU, SUBMITPAGE, DATABASE = 0, 1, 2, 3, 4, 5

# Button Setup
button0 = RoundButton.RoundButton('roundButton3.png', 'roundButton4.png', 10, 10, 47, 41)
button1 = Button.Button("Sign In", 100, 300, 160, 60, )
button2 = Button.Button("Sign Up", 100, 400, 160, 60, )
button3 = RoundButton.RoundButton('roundButton1.png', 'roundButton2.png', 50, 150, 275, 277)
button4 = Button.Button("Database", 100, 480, 160, 60, )
button5 = Button.Button("Submit", 100, 600, 160, 60, )
button6 = Button.Button("Enter", 100, 500, 160, 60, )

# Text Setup
FONT = pygame.font.SysFont("arial", 30)
FONT2 = pygame.font.SysFont("arial", 15)
txt1 = FONT.render("Flood Feedback", True, "white")
txt2 = FONT2.render('Enter Flood Duration', True, "black")
txt3 = FONT2.render('Enter Flood Height', True, "black")
txt4 = FONT2.render('Enter Latitue, Longitude', True, "black")
txt5 = FONT2.render('Password Incorrect', True, "red")
txt6 = FONT2.render('Username Not Found', True, "red")
txt7 = FONT2.render('Username Taken', True, "red")
txt8 = FONT2.render('Username Or Password Invalid', True, "red")
txt9 = FONT2.render('Enter Username:', True, "black")
txt10 = FONT2.render('Enter Password:', True, "black")

# Get list of usernames and passwords from file
userdata = {}
with open('Userdata') as file:
    for line in file:
        userdata[line.split()[0]] = line.split()[1][0:-1]

#ip = geocoder.ip("me")
#latlng = str(ip.latlng)
#latlng = '[51.779701, -108.413872]'
#latlngtxt = FONT2.render('Latitue, Longitude: ' + latlng, True, "black")



def main() -> None:
    # variable setup
    run = True
    screen = 0
    latlng = ''
    latlngin = InputBox.InputBox(latlng, 40, 160, 280, 25)
    duration = ''
    durationin = InputBox.InputBox(duration, 40, 220, 280, 25)
    height = ''
    heightin = InputBox.InputBox(height, 40, 280, 280, 25)
    username = ''
    usernamein = InputBox.InputBox(username, 40, 160, 280, 25)
    password = ''
    passwordin = InputBox.InputBox(password, 40, 220, 280, 25)
    usernametxt = FONT2.render('Username: ' + username, True, "black")
    todaydate = str(datetime.date.today())
    todaydatetxt = FONT2.render('Date: ' + todaydate, True, "black")
    clock = pygame.time.Clock()

    # main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the close button is clicked
                run = False
                break
            mouse_pos = pygame.mouse.get_pos()
            if screen == START:
                Window.fill((25, 25, 112))
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

            elif screen == SIGNIN:
                Window.fill((255, 213, 128))
                Window.blit(txt9, (40, 140))
                usernamein.draw(Window, username)
                Window.blit(txt10, (40, 200))
                passwordin.draw(Window, password)
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if button6.is_hovered(mouse_pos):
                    button6.draw(Window, (230, 230, 230))
                else:
                    button6.draw(Window, 'WHITE')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 0
                    elif button6.is_clicked(event):
                        if username in userdata:
                            if password == userdata[username]:
                                screen = 3
                                usernametxt = FONT2.render('Username: ' + username, True, "black")
                            else:
                                Window.blit(txt5, (40, 400))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                username = ''
                                password = ''
                        else:
                            Window.blit(txt6, (40, 400))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                            username = ''
                            password = ''
                        usernamein.isselected = False
                        passwordin.isselected = False

                    elif usernamein.is_clicked(event):
                        usernamein.isselected = True
                        passwordin.isselected = False
                    elif passwordin.is_clicked(event):
                        usernamein.isselected = False
                        passwordin.isselected = True
                elif event.type == pygame.KEYDOWN:
                    if usernamein.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            username = username[0:-1]
                        else:
                            username += event.unicode
                    elif passwordin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            password = password[0:-1]
                        else:
                            password += event.unicode

            elif screen == SIGNUP:
                Window.fill((255, 213, 128))
                Window.blit(txt9, (40, 140))
                usernamein.draw(Window, username)
                Window.blit(txt10, (40, 200))
                passwordin.draw(Window, password)
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if button6.is_hovered(mouse_pos):
                    button6.draw(Window, (230, 230, 230))
                else:
                    button6.draw(Window, 'WHITE')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 0
                    elif button6.is_clicked(event):
                        if not (username in userdata):
                            if password != '' and username != '' and not (' ' in password) and not (' ' in username):
                                screen = 3
                                usernametxt = FONT2.render('Username: ' + username, True, "black")
                                f = open("Userdata", "a")
                                f.write(username + ' ' + password + '\n')
                                f.close()
                            else:
                                Window.blit(txt8, (40, 400))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                username = ''
                                password = ''
                        else:
                            Window.blit(txt7, (40, 400))
                            pygame.display.flip()
                            pygame.time.wait(1000)
                            username = ''
                            password = ''
                        usernamein.isselected = False
                        passwordin.isselected = False
                    elif usernamein.is_clicked(event):
                        usernamein.isselected = True
                        passwordin.isselected = False
                    elif passwordin.is_clicked(event):
                        usernamein.isselected = False
                        passwordin.isselected = True
                elif event.type == pygame.KEYDOWN:
                    if usernamein.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            username = username[0:-1]
                        else:
                            username += event.unicode
                    elif passwordin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            password = password[0:-1]
                        else:
                            password += event.unicode

            elif screen == MENU:
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

            elif screen == SUBMITPAGE:
                Window.fill((255, 213, 128))
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if button5.is_hovered(mouse_pos):
                    button5.draw(Window, (230, 230, 230))
                else:
                    button5.draw(Window, 'WHITE')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 3
                    elif button5.is_clicked(event):
                        f = open("Database", "a")
                        f.write("User: " + username + '\n')
                        f.write("Latitute, longitude: " + latlng + '\n')
                        f.write("Date: " + todaydate + '\n')
                        f.write("Duration: " + duration + '\n')
                        f.write("Height: " + height + '\n')
                        f.write('\n')
                        f.close()
                        latlng = ''
                        duration = ''
                        height = ''
                        latlngin.isselected = False
                        durationin.isselected = False
                        heightin.isselected = False
                    elif latlngin.is_clicked(event):
                        latlngin.isselected = True
                        durationin.isselected = False
                        heightin.isselected = False
                    elif durationin.is_clicked(event):
                        latlngin.isselected = False
                        durationin.isselected = True
                        heightin.isselected = False
                    elif heightin.is_clicked(event):
                        latlngin.isselected = False
                        durationin.isselected = False
                        heightin.isselected = True
                elif event.type == pygame.KEYDOWN:
                    if latlngin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            latlng = latlng[0:-1]
                        else:
                            latlng += event.unicode
                    elif durationin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            duration = duration[0:-1]
                        else:
                            duration += event.unicode
                    elif heightin.isselected:
                        if event.key == pygame.K_BACKSPACE:
                            height = height[0:-1]
                        else:
                            height += event.unicode

                Window.blit(usernametxt, (40, 70))
                Window.blit(todaydatetxt, (40, 100))
                Window.blit(txt4, (40, 140))
                Window.blit(txt2, (40, 200))
                Window.blit(txt3, (40, 260))
                latlngin.draw(Window, latlng)
                durationin.draw(Window, duration)
                heightin.draw(Window, height)

            elif screen == DATABASE:
                Window.fill('WHITE')
                i = 0
                with open('Database') as file:
                    for line in file:
                        t = FONT2.render(line[0:len(line) - 1], True, "black")
                        Window.blit(t, (5, 100 + i * 15))
                        i += 1
                if button0.is_hovered(mouse_pos):
                    button0.draw(Window, True)
                else:
                    button0.draw(Window, False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button0.is_clicked(event):
                        screen = 3

        pygame.display.flip()  # Update the display with the drawn frame
        clock.tick(60)


if __name__ == "__main__":
    main()
