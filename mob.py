import pygame as pg
import random
import math
from os import *
from settings import *

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.clase = "Felltwin"
        self.movement_dict = {
                              "up": [0, -1],
                              "down": [0, 1],
                              "right": [1, 0],
                              "left": [-1, 0]
                             }

        self.current_frame = 0
        self.last_folder = "down"
        self.last_update = 0
        self.img_dir = path.join(path.join(game_folder, "img\Enemies"), self.clase)
        self.images = self.get_images(path.join(self.img_dir, "Movement\down"))
        self.image = self.images[self.current_frame]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 0)

    def update(self):
        self.speed = [0, 0]
        self.foldername = ""
        self.detect()

        self.rect.y += self.speed[1]
        self.rect.x += self.speed[0]
        # if self.rect.bottom > HEIGHT:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0

    def detect(self):
        if math.sqrt((self.rect.centerx - self.game.player.rect.centerx) ** 2 + (self.rect.centery - self.game.player.rect.centery) ** 2) < 500:
            self.follow()

    def follow(self):
        self.choque = False
        difference = 80
        if self.rect.left <= self.game.player.rect.right - difference and self.rect.right >= self.game.player.rect.left + difference:
            if self.rect.bottom == self.game.player.rect.top + difference:
                self.choque = True
                self.speed = [0, 0]
                self.attack()
            elif self.rect.top == self.game.player.rect.bottom - difference:
                self.choque = True
                self.speed = [0, 0]
                self.attack()

        if self.rect.top <= self.game.player.rect.bottom - difference and self.rect.bottom >= self.game.player.rect.top + difference:
            if self.rect.left == self.game.player.rect.right - difference:
                self.choque = True
                self.speed = [0, 0]
                self.attack()
            elif self.rect.right == self.game.player.rect.left + difference:
                self.choque = True
                self.speed = [0, 0]
                self.attack()

        if self.rect.centerx > self.game.player.rect.centerx and not self.choque:
            if self.rect.centery > self.game.player.rect.centery:
                self.speed = [-1, -1]
                self.move("upleft")
            elif self.rect.centery < self.game.player.rect.centery:
                self.speed = [-1, 1]
                self.move("downleft")
            else:
                self.speed = [-1, 0]
                self.move("left")
        elif self.rect.centerx < self.game.player.rect.centerx and not self.choque:
            if self.rect.centery > self.game.player.rect.centery:
                self.speed = [1, -1]
                self.move("upright")
            elif self.rect.centery < self.game.player.rect.centery:
                self.speed = [1, 1]
                self.move("downright")
            else:
                self.speed = [1, 0]
                self.move("right")
        elif not self.choque:
            if self.rect.centery > self.game.player.rect.centery:
                self.speed = [0, -1]
                self.move("up")
            elif self.rect.centery < self.game.player.rect.centery:
                self.speed = [0, 1]
                self.move("down")

    def attack(self):
        pass
    '''
        attack_dir = path.join(self.img_dir, "Attacks")
        isattacking = False
        actionkeyspressed = self.keys.get_keynames(self.keys.action_keyspressed)
        for keyname in actionkeyspressed:
            self.speed = [0, 0]
        if len(actionkeyspressed) > 0:
            folder = path.join(attack_dir, self.last_folder)
            isattacking = True
            self.action(folder)

        return isattacking
    '''

    def standing(self, folder):
        stand_dir = ""
        stand_dir = path.join(self.img_dir, "Standing")
        stand_dir = path.join(stand_dir, folder)
        self.action(stand_dir)

    def folder_check(self, folder):
        spc = " "
        index = folder.index(spc) if spc in folder else None
        if index != None:
            s1 = folder[0:index]
            s2 = folder[(index + 1):len(folder)]
            if s2 == "up" or s2 == "down":
                folder = s2 + s1
            else:
                folder = s1 + s2

        return folder

    def move(self, foldername):
        mov_dir = path.join(self.img_dir, "Movement")
        folder = ""
        folder = path.join(mov_dir, foldername)
        #ismoving = False
        self.action(folder)

        #return folder, ismoving

    def get_images(self, frames_dir):
        files_range = listdir(frames_dir)
        images = []
        for i in range(len(files_range) - 1):
            images.append(pg.image.load(path.join(frames_dir, str(i) + ".png")))
            images[i].set_colorkey(WHITE)
        return images

    def action(self, folder):
        self.images = self.get_images(folder)
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
