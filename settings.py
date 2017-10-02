# game options/settings
from os import path

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
LIGHT_BLACK = (60, 60, 55)
DARK_GREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
DOWN_RED = (216, 40, 35)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
COLORKEY = (34, 177, 76)


INTRO_TITLE = "DOOM KINGDOM"
TITLE = "Zombie"
WIDTH = 800
HEIGHT = 600
TILESIZE = 32
BGCOLOR = DARK_GREY
FPS = 60
game_folder = path.dirname(__file__)
IMAGE_FOLDER = "img"


# Player Settings
PLAYER_SPRITESHEET = "%s in %s.png"
PLAYER_SPEED = 2
