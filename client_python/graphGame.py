from pygame import gfxdraw
from pygame import *
from game import *
import pygame
from client import *
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

FONT = pygame.font.SysFont('Arial', 20, bold=True)
clock = pygame.time.Clock()
pygame.font.init()
pygame.display.set_caption("Pokemon Game")


class graphGame:
    def __init__(self, game: game()):
        self.game = game
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

        self.POKEMON = pygame.transform.scale(pygame.image.load("pokemon.png"), (self.screen.get_width(), self.screen.get_height()))
        POKEMON1 = pygame.transform.scale(pygame.image.load("pokemon1.png"), (40, 40))
        POKEMON2 = pygame.transform.scale(pygame.image.load("pokemon2.png"), (40, 40))
        POKEMON3 = pygame.transform.scale(pygame.image.load("pokemon3.png"), (40, 40))
        self.ASH = pygame.transform.scale(pygame.image.load("ash.png"), (60, 60))
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

    def my_scale(self,data, x=False, y=False):
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

            # id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            # rect = id_srf.get_rect(center=(x, y))
            # self.screen.blit(id_srf, rect)

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

    def draw_agent(self):
        agents = self.game.agents
        for agent in agents:
            x, y = agent.pos[0],agent.pos[1]
            x = self.my_scale(float(x), x = True)
            y = self.my_scale(float(y), y = True)
            self.screen.blit(self.ASH, (int(x) - 28, int(y) - 28))


    def draw_pokemon(self):
        pokemons = self.game.pokemons
        for p in pokemons:
            x, y = p.pos[0], p.pos[1]
            x = self.my_scale(float(x), x=True)
            y = self.my_scale(float(y), y=True)
            self.screen.blit(self.LIST[2], (int(x) - 18, int(y) - 18))


    def draw_move(self):
        number_of_move = MOVE_FONT.render("Move: " + str(client.move), 1, WHITE)
        self.screen.blit(number_of_move, (self.screen.get_width() - 500, self.screen.get_height() - 30))


    def main(self):
        self.screen.fill(BLACK)
        back = pygame.transform.scale(pygame.image.load("pokemon.png"),
                                           (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(back, [0,0])
        # move = client.get_info().split(",")
        # move = move[2].split(":")[1]
        self.draw_edges()
        self.draw_node()
        self.draw_agent()
        self.draw_pokemon()
        self.draw_move()
        display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False


class Button:
    def __init__(self, color, rect: pygame.Rect):
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed

button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))