import os
from os import path
from settings import *
import pygame
from Tutorial import *

def Intro(self):

    img_dir = path.join(game_folder, "img")

    clock = pygame.time.Clock()

    #font = pygame.font.SysFont("Arial", 35)
    GameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.image.load(path.join(img_dir, "background.jpg")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    #img_dir = path.join(game_folder, "img")

    titu = pygame.image.load(path.join(img_dir, "logo1.png")).convert()
    titu.set_colorkey(BLACK)
    #titu = pygame.transform.scale(titu, (WIDTH, HEIGHT))
    titu_rect = titu.get_rect()
    #titu.rect.top

    def text_button(text, font, color):
        textbutton = font.render(text, True, color)
        return textbutton, textbutton.get_rect()

    def button_iniciar(x, y, width, height, text, events, hover_color, color):
        #Getting mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Creating the button
        r = pygame.Rect(x, y, width, height)
        r.center = (x/2, y/2)
        #If mouse is hovering the button, light it up
        if r.x <= mouse[0] <= r.x + width and r.y <= mouse[1] <= r.y + height:
            pygame.draw.rect(GameDisplay, hover_color, r)
            if click[0] == 1:
                self.run()
        else:
            pygame.draw.rect(GameDisplay, color, r)

        #Creating text for the button
        font = pygame.font.SysFont("Arial", 25)
        textbutton, textrect = text_button(text, font, WHITE)
        #Centering text
        textrect.center = (r.x + (width/2), r.y + (height/2))

        GameDisplay.blit(textbutton, textrect)


    def button_tutorial(x, y, width, height, text, events, hover_color, color):
        #Getting mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Creating the button
        r = pygame.Rect(x, y, width, height)
        r.center = (x/2, y/1.5)
        #If mouse is hovering the button, light it up
        if r.x <= mouse[0] <= r.x + width and r.y <= mouse[1] <= r.y + height:
            pygame.draw.rect(GameDisplay, hover_color, r)
            if click[0] == 1:
                tutorial()
        else:
            pygame.draw.rect(GameDisplay, color, r)

        #Creating text for the button
        font = pygame.font.SysFont("Arial", 25)
        textbutton, textrect = text_button(text, font, WHITE)
        #Centering text
        textrect.center = (r.x + (width/2), r.y + (height/2))

        GameDisplay.blit(textbutton, textrect)

    def button_salir(x, y, width, height, text, events, hover_color, color):
        #Getting mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Creating the button
        r = pygame.Rect(x, y, width, height)
        r.center = (x/2, y/1.2)
        #If mouse is hovering the button, light it up
        if r.x <= mouse[0] <= r.x + width and r.y <= mouse[1] <= r.y + height:
            pygame.draw.rect(GameDisplay, hover_color, r)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(GameDisplay, color, r)

        #Creating text for the button
        font = pygame.font.SysFont("Arial", 25)
        textbutton, textrect = text_button(text, font, WHITE)
        #Centering text
        textrect.center = (r.x + (width/2), r.y + (height/2))

        GameDisplay.blit(textbutton, textrect)


    done = False

    while not done:

        events = pygame.event.get()
        mouse = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        GameDisplay.fill(WHITE)
        GameDisplay.blit(background, background_rect)
        GameDisplay.blit(titu, titu_rect)
        #button(x, y, width, height, text, event, hover_color, color)
        button_iniciar(WIDTH, HEIGHT, 150, 50, "Nueva Partida", events, DOWN_RED, LIGHT_BLACK)
        button_tutorial(WIDTH, HEIGHT, 150, 50, "Tutorial", events, DOWN_RED, LIGHT_BLACK)
        button_salir(WIDTH, HEIGHT, 150, 50, "Salir", events, DOWN_RED, LIGHT_BLACK)
        #game_title, game_title_rect = text_button(INTRO_TITLE, font, RED)
        #game_title_rect.center = (WIDTH/2, HEIGHT/4 + 30)
        #GameDisplay.blit(game_title, game_title_rect)

        pygame.display.update()
