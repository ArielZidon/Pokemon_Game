import random
import pygame
import os
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
from pygame import *
import pygame
import sys
from pygame.locals import *
pygame.font.init()
pygame.mixer.init()

# init pygame
WIDTH, HEIGHT = 1080, 720

FPS = 60

# default port
PORT = 6666

# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
YELLOW = (255, 255, 0)

MOVE_FONT = pygame.font.SysFont('comicsans', 20)

client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

radius = 15

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

client.start()

graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)

graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

# POKEMON = pygame.transform.scale(pygame.image.load(os.path.join('client_python', 'pokemon.png')), (WIDTH, HEIGHT))
# screen.blit(POKEMON, (0, 0))

# POKEMON = pygame.transform.scale(pygame.image.load("pokemon.png"), (screen.get_width(), screen.get_height()))

# POKEMON_IMAGE = image.load(POKEMON)

POKEMON1 = pygame.transform.scale(pygame.image.load("pokemon1.png"), (40, 40))
POKEMON2 = pygame.transform.scale(pygame.image.load("pokemon2.png"), (40, 40))
POKEMON3 = pygame.transform.scale(pygame.image.load("pokemon3.png"), (40, 40))

LIST = (POKEMON1, POKEMON2, POKEMON3)

pygame.display.set_caption("Pokemon Game")


for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y

def draw_Button():
    pygame.draw.rect(screen, button.color, button.rect)
    button_text = FONT.render("Exit", True, (210, 56, 23))
    screen.blit(button_text, (button.rect.x+20, button.rect.y+10))

def draw_move(move: int):
    number_of_move = MOVE_FONT.render("Move: " + str(move), 1, WHITE)
    screen.blit(number_of_move, (screen.get_width()-110, screen.get_height()-30))

    pygame.display.update()

def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


def draw_agent(agents):
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23),
                           (int(agent.pos.x), int(agent.pos.y)), 10)

def draw_pokemon(pokemons):
    for p in pokemons:
        # pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
        screen.blit(POKEMON3, (int(p.pos.x)-18, int(p.pos.y)-18))

def draw_node():
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

def draw_edges():
    for e in graph.Edges:
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))

class Button:
    def __init__(self, color, rect: pygame.Rect):
        self.color = color
        self.rect = rect
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed

button = Button(color=(0, 0, 0), rect=pygame.Rect((10, 10), (100, 50)))

def main():

    while client.is_running() == 'true':
        POKEMON = pygame.transform.scale(pygame.image.load("pokemon.png"), (screen.get_width(), screen.get_height()))
        clock.tick(FPS)
        move = client.get_info().split(",")
        move = move[2].split(":")[1]

        pokemons = json.loads(client.get_pokemons(),
                              object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        agents = json.loads(client.get_agents(),
                            object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]
        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                button.press()
                if button.pressed:
                    pygame.quit()
                    exit(0)

        screen.fill(BLACK)
        # POKEMON_IMAGE = transform.scale(POKEMON_IMAGE, (screen.get_width(), screen.get_height()))
        screen.blit(POKEMON, (0, 0))
        draw_node()
        draw_edges()
        draw_agent(agents)
        draw_pokemon(pokemons)
        draw_Button()
        draw_move(move)

        # refresh surface
        pygame.display.update()

        # draw_node()
        # draw_edges()
        # draw_agent(agents)
        # draw_pokemon(pokemons)

        # update screen changes
        # display.update()

        # choose next edge
        for agent in agents:
            if agent.dest == -1:
                next_node = (agent.src - 1) % len(graph.Nodes)
                client.choose_next_edge(
                    '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
                ttl = client.time_to_end()
                print(ttl, client.get_info())
        client.move()
    # game over:

if __name__ == "__main__":
    main()