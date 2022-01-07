import time
from pygame import gfxdraw
from pygame import *
from game import *
import pygame
from client import *
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()
from Pokemon_im import *

client = Client()

WIDTH, HEIGHT = 1080, 720
FPS = 60
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MOVE_FONT = pygame.font.SysFont('comicsans', 20)
FONT = pygame.font.SysFont('Arial', 20, bold=True)
FONT_END = pygame.font.SysFont('comicsans', 55, bold=True)

radius = 15

clock = pygame.time.Clock()
pygame.font.init()
pygame.display.set_caption("Pokemon Game")


class graphGame:
    def __init__(self, game: game()):
        self.game = game
        self.COUNT = 0
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

        self.POKEMON = pygame.transform.scale(pygame.image.load("../Pokemon_im/pokemon.png"), (self.screen.get_width(), self.screen.get_height()))
        POKEMON1 = pygame.transform.scale(pygame.image.load("../Pokemon_im/pokemon1.png"), (40, 40))
        POKEMON2 = pygame.transform.scale(pygame.image.load("../Pokemon_im/pokemon2.png"), (40, 40))
        POKEMON3 = pygame.transform.scale(pygame.image.load("../Pokemon_im/pokemon3.png"), (40, 40))
        self.ASH = pygame.transform.scale(pygame.image.load("../Pokemon_im/ash.png"), (60, 60))
        self.ASH1 = pygame.transform.scale(pygame.image.load("../Pokemon_im/ash1.png"), (60, 60))
        self.ASH2 = pygame.transform.scale(pygame.image.load("../Pokemon_im/ash2.png"), (40, 40))
        self.ASH_LIST = (self.ASH, self.ASH1, self.ASH2)
        self.LIST = (POKEMON1, POKEMON2, POKEMON3)
        self.min_x = float('inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.max_x = float('-inf')
        for n in self.game.graph.nodes.values():
            x = n.pos[0]
            y = n.pos[1]
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height()-50, self.min_y, self.max_y)

    def draw_node(self):
        graph_o = self.game.graph
        for n in graph_o.nodes.values():
            x = self.my_scale(n.pos[0], x=True)
            y = self.my_scale(n.pos[1], y=True)
            gfxdraw.filled_circle(self.screen, int(x), int(y), radius, Color(64, 80, 174))
            gfxdraw.aacircle(self.screen, int(x), int(y), radius, Color(255, 255, 255))

            id_srf = FONT.render(str(n.key), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            self.screen.blit(id_srf, rect)

    def draw_edges(self):
        graph = self.game.graph
        for i in graph.edges.keys():
            src = graph.nodes[i[0]]
            dest = graph.nodes[i[1]]
            src_x = self.my_scale(src.pos[0], x=True)
            src_y = self.my_scale(src.pos[1], y=True)
            dest_x = self.my_scale(dest.pos[0], x=True)
            dest_y = self.my_scale(dest.pos[1], y=True)
            pygame.draw.line(self.screen, Color(WHITE), (src_x, src_y), (dest_x, dest_y), width=5)

    def draw_agent(self, size: int):
        agents = self.game.agents
        size -= 1
        for agent in agents:
            x, y = agent.pos[0],agent.pos[1]
            x = self.my_scale(float(x), x = True)
            y = self.my_scale(float(y), y = True)
            # self.screen.blit(self.ASH, (int(x) - 28, int(y) - 28))
            # self.screen.blit(self.ASH1, (int(x) - 28, int(y) - 28))
            if size == 2:
                self.screen.blit(self.ASH_LIST[size], (int(x) - 21, int(y) - 21))
            if size == 1:
                self.screen.blit(self.ASH_LIST[size], (int(x) - 29, int(y) - 29))
            if size == 0:
                self.screen.blit(self.ASH_LIST[size], (int(x) - 28, int(y) - 28))
            size -= 1


    def draw_pokemon(self):
        pokemons = self.game.pokemons
        for p in pokemons:
            x, y = p.pos[0], p.pos[1]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)
            if (p.type > 0):
                self.screen.blit(self.LIST[2], (int(x) - 18, int(y) - 18))
            else:
                self.screen.blit(self.LIST[1], (int(x) - 18, int(y) - 18))

    def draw_Button(self):
        pygame.draw.rect(self.screen, button.color, button.rect)
        button_text = FONT.render("Exit", True, (210, 56, 23))
        self.screen.blit(button_text, (button.rect.x + 20, button.rect.y + 10))

    def draw_move(self, move: int):
        number_of_move = MOVE_FONT.render("Move: " + str(move), True, BLUE)
        self.screen.blit(number_of_move, (self.screen.get_width() - 110, self.screen.get_height() - 30))

    def draw_ttl(self, ttl: int):
        number_of_move = MOVE_FONT.render("Time to live: " + str(ttl)+" second", True, WHITE)
        self.screen.blit(number_of_move, (10, self.screen.get_height() - 30))

    def draw_grade(self, grade: int):
        number_of_move = MOVE_FONT.render("Grade: " + str(grade), True, GREEN)
        self.screen.blit(number_of_move, (self.screen.get_width() - 110, 10))


    def main(self, move, ttl, grade, size):
        self.screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.press()
                    if button.pressed:
                        pygame.quit()
                        exit(0)
        if ttl == 0:
            self.screen.fill(BLACK)
            game_end = FONT_END.render("GAME OVER !", True, RED)
            button_text = FONT_END.render("Results: your grade is - "+grade, True, WHITE)
            self.screen.blit(game_end, (self.screen.get_width()/3, 10))
            self.screen.blit(button_text, (self.screen.get_width()/6.3, self.screen.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()
            exit(0)


        self.screen.fill(BLACK)
        back = pygame.transform.scale(pygame.image.load("../Pokemon_im/pokemon.png"),
                                      (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(back, [0, 0])
        self.draw_edges()
        self.draw_node()
        self.draw_agent(size)
        self.draw_pokemon()
        self.draw_move(move)
        self.draw_ttl(ttl)
        self.draw_grade(grade)
        self.draw_Button()
        display.update()


class Button:
    def __init__(self, color, rect: pygame.Rect):
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed

button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))