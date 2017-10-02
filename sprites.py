import pygame as pg
import random
from os import *
from settings import *
import math
vec = pg.math.Vector2

class SpriteSheet:
    def __init__(self, folder, filename):
        self.image_dir = path.join(game_folder, IMAGE_FOLDER)
        self.spritesheet = pg.image.load(path.join(path.join(self.image_dir, folder),filename)).convert()

    def get_image(self, x, y, width, height, img_x = 16, img_y = 16):
        image = pg.Surface((128, 128))
        image.fill(WHITE)
        image.blit(self.spritesheet, (img_x, img_y), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.clase = "Warrior"
        self.load_images()
        self.current_frame = 0
        self.last_dir = "down"
        self.last_update = 0
        self.image = self.player_movement["down"][0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)

    def load_images(self):
        self.spritesheet = SpriteSheet("Class\\" + self.clase, PLAYER_SPRITESHEET %(self.clase, "Light Armor with Sword & Shield"))
        self.player_movement = {"down": [],
                                "downleft": [],
                                "left": [],
                                "upleft": [],
                                "up": [],
                                "upright": [],
                                "right": [],
                                "downright": []}
        y = 1045
        for key in self.player_movement:
            for x in range(3651, 4419, 96):
                self.player_movement[key].append(self.spritesheet.get_image(x, y, 96, 96))
            y += 97

        self.player_attack = {"down": [],
                              "downleft": [],
                              "left": [],
                              "upleft": [],
                              "up": [],
                              "upright": [],
                              "right": [],
                              "downright": []}

        y = 7
        for key in self.player_attack:
            for x in range(0, 2048, 128):
                self.player_attack[key].append(self.spritesheet.get_image(x, y, 128, 128, 0, -12))
            y += 129

        self.player_standing = {"down": [],
                              "downleft": [],
                              "left": [],
                              "upleft": [],
                              "up": [],
                              "upright": [],
                              "right": [],
                              "downright": []}
        y = 1045
        for key in self.player_standing:
            for x in range(961, 2881, 96):
                self.player_standing[key].append(self.spritesheet.get_image(x, y, 96, 96))
            y += 97

    def move(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
        if keys[pg.K_UP]:
            if keys[pg.K_RIGHT]:
                self.action(self.player_movement, "upright")
            elif keys[pg.K_LEFT]:
                self.action(self.player_movement, "upleft")
            else:
                self.action(self.player_movement, "up")
        if keys[pg.K_DOWN]:
            if keys[pg.K_RIGHT]:
                self.action(self.player_movement, "downright")
            elif keys[pg.K_LEFT]:
                self.action(self.player_movement, "downleft")
            else:
                self.action(self.player_movement, "down")
        if keys[pg.K_LEFT]:
            if keys[pg.K_UP]:
                self.action(self.player_movement, "upleft")
            elif keys[pg.K_DOWN]:
                self.action(self.player_movement, "downleft")
            else:
                self.action(self.player_movement, "left")
        if keys[pg.K_RIGHT]:
            if keys[pg.K_UP]:
                self.action(self.player_movement, "upright")
            elif keys[pg.K_DOWN]:
                self.action(self.player_movement, "downright")
            else:
                self.action(self.player_movement, "right")

    def attack(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_q]:
            self.ismoving = False
            self.vel = (0, 0)
            
            self.action(self.player_attack, self.last_dir)
        else:
            self.ismoving = True

    def update(self):
        self.vel = vec(0, 0)
        self.attack()
        if self.ismoving:
            self.move()
        if self.ismoving and self.vel == [0, 0]:
            self.action(self.player_standing, self.last_dir)
        self.pos += self.vel
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def action(self, action_type, action_dir):
        self.last_dir = action_dir
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(action_type[action_dir])
            self.image = action_type[action_dir][self.current_frame]

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.clase = "Felltwin"
        self.load_images()
        self.current_frame = 0
        self.last_dir = "down"
        self.last_update = 0
        self.image = self.mob_movement["down"][self.current_frame]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(WIDTH / 2, 0)
        self.rect.center = self.pos

    def load_images(self):
        self.spritesheet = SpriteSheet("Enemies\\" + self.clase, self.clase + ".png")
        self.mob_movement = {"down": [],
                             "downleft": [],
                             "left": [],
                             "upleft": [],
                             "up": [],
                             "upright": [],
                             "right": [],
                             "downright": []}
        y = 1045
        for key in self.mob_movement:
            for x in range(3074, 4738, 128):
                self.mob_movement[key].append(self.spritesheet.get_image(x, y, 128, 128, 0, 0))
            y += 129

        self.mob_attack = {"down": [],
                           "downleft": [],
                           "left": [],
                           "upleft": [],
                           "up": [],
                           "upright": [],
                           "right": [],
                           "downright": []}

        y = 7
        for key in self.mob_attack:
            for x in range(0, 2048, 128):
                self.mob_attack[key].append(self.spritesheet.get_image(x, y, 128, 128, 0, -12))
            y += 129

        self.mob_standing = {"down": [],
                             "downleft": [],
                             "left": [],
                             "upleft": [],
                             "up": [],
                             "upright": [],
                             "right": [],
                             "downright": []}
        y = 1045
        for key in self.mob_standing:
            for x in range(961, 2881, 96):
                self.mob_standing[key].append(self.spritesheet.get_image(x, y, 96, 96))
            y += 97

    def update(self):
        self.vel = vec(0, 0)
        self.detect()
        self.pos += self.vel
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y
        # if self.rect.bottom > HEIGHT:
        #     self.rect.right = WIDTH
        # if self.rect.left < 0:
        #     self.rect.left = 0

    def detect(self):
        if math.sqrt((self.rect.centerx - self.game.player.rect.centerx) ** 2 + (self.rect.centery - self.game.player.rect.centery) ** 2) < 500:
            self.follow()

    def follow(self):
        self.choque = False
        offset_top = 64
        offset_side = 96
        offset_y_right = 20
        offset_y_left = 16
        if self.rect.left <= self.game.player.rect.right - offset_side and self.rect.right >= self.game.player.rect.left + offset_side:
            if self.rect.bottom == self.game.player.rect.top + offset_top:
                self.choque = True
                self.vel = [0, 0]
                self.attack()
            elif self.rect.top == self.game.player.rect.bottom - offset_top:
                self.choque = True
                self.vel = [0, 0]
                self.attack()

        if self.rect.top <= self.game.player.rect.bottom - offset_top and self.rect.bottom >= self.game.player.rect.top + offset_top:
            if self.rect.left == self.game.player.rect.right - offset_side:
                self.choque = True
                self.vel = [0, 0]
                self.attack()
            elif self.rect.right == self.game.player.rect.left + offset_side:
                self.choque = True
                self.vel = [0, 0]
                self.attack()

        if self.rect.centerx > self.game.player.rect.centerx and not self.choque:
            if self.rect.centery > self.game.player.rect.centery - offset_y_left:
                self.vel.x = -MOB_SPEED
                self.vel.y = -MOB_SPEED
                self.action(self.mob_movement, "upleft")
            elif self.rect.centery < self.game.player.rect.centery - offset_y_left:
                self.vel.x = -MOB_SPEED
                self.vel.y = MOB_SPEED
                self.action(self.mob_movement, "downleft")
            else:
                self.vel.x = -MOB_SPEED
                self.action(self.mob_movement, "left")
        elif self.rect.centerx < self.game.player.rect.centerx and not self.choque:
            if self.rect.centery > self.game.player.rect.centery - offset_y_right:
                self.vel.x = MOB_SPEED
                self.vel.y = -MOB_SPEED
                self.action(self.mob_movement, "upright")
            elif self.rect.centery < self.game.player.rect.centery - offset_y_right:
                self.vel.x = MOB_SPEED
                self.vel.y = MOB_SPEED
                self.action(self.mob_movement, "downright")
            else:
                self.vel.x = MOB_SPEED
                self.action(self.mob_movement, "right")
        elif not self.choque:
            if self.rect.centery > self.game.player.rect.centery:
                self.vel.y = -MOB_SPEED
                self.action(self.mob_movement, "up")
            elif self.rect.centery < self.game.player.rect.centery:
                self.vel.y = MOB_SPEED
                self.action(self.mob_movement, "down")

    def attack(self):
        pass

    def action(self, action_type, action_dir):
        self.last_dir = action_dir
        now = pg.time.get_ticks()
        if now - self.last_update > 100:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(action_type[action_dir])
            self.image = action_type[action_dir][self.current_frame]
