from os import path
from settings import *

class Image:
    def __init__(self):
        self.dir = path.join(game_folder, "img")

    def get_images(self, frames_dir):
        frames = path.join(self.dir, frames_dir)
        files_range = listdir(frames)
        self.list = []
        for i in range(len(files_range) - 1):
            self.list.append(pg.image.load(path.join(frames, str(i) + ".png")))
            self.list[i].set_colorkey(BLACK)

        return images

    def set_class_dir(self, dest):
        self.dir = path.join(self.dir, dest)
