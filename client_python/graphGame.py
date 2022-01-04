import random
import pygame
import os
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
from pygame import *
from game import *
import pygame
import sys
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1080, 720
FPS = 60
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
YELLOW = (255, 255, 0)

MOVE_FONT = pygame.font.SysFont('comicsans', 20)

radius = 15

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

FONT = pygame.font.SysFont('Arial', 20, bold=True)

clock = pygame.time.Clock()
pygame.font.init()


LIST = (POKEMON1, POKEMON2, POKEMON3)

pygame.display.set_caption("Pokemon Game")

class Button:
    def __init__(self, color, rect: pygame.Rect):
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed

button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))

class graphGame:
    def __init__(self, game: game):
        self.game = game
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

        POKEMON = pygame.transform.scale(pygame.image.load("pokemon.png"), (screen.get_width(), screen.get_height()))
        POKEMON1 = pygame.transform.scale(pygame.image.load("pokemon1.png"), (40, 40))
        POKEMON2 = pygame.transform.scale(pygame.image.load("pokemon2.png"), (40, 40))
        POKEMON3 = pygame.transform.scale(pygame.image.load("pokemon3.png"), (40, 40))
        ASH = pygame.transform.scale(pygame.image.load("ash.png"), (40, 40))

        self.min_x = float('inf')*-1
        self.min_y = flaot('inf')*-1
        self.max_y = float('inf')
        self.max_x = float('inf')

        for n in game.graph.nodes:
            x = n.pos[0]
            y = n.pos[1]
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)

    def scale(data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(data, x=False, y=False):
        if x:
            return scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, screen.get_height()-50, min_y, max_y)

    def draw_node(self):
        graph_node = self.game.graph
        for n in graph_node:
            x = my_scale(n.pos[0], x=True)
            y = my_scale(n.pos[1], y=True)
            gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(189, 74, 184))
            gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 255))

            id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)


    def main(self):
        self.screen = pygame.transform.scale(pygame.image.load("pokemon.png"), (screen.get_width(), screen.get_height()))