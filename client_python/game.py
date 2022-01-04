from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from argoments import *
import json
from client import *
from client import *
from GraphAlgo import GraphAlgo
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

import subprocess
import sys

from client import Client

# """sys.argv[1]"""
# subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {0}'])
# # default port
# PORT = 6666
# # server host (default localhost 127.0.0.1)
# HOST = '127.0.0.1'
client = Client()


# client.start_connection(HOST, PORT)
# client.add_agent("{\"id\":0}")
#

class game:
    def __init__(self) -> None:
        self.graph = DiGraph()
        self.pokemons = []
        self.agents = []

    def up_to_serv(self, pokemons=None, agents=None, graph=None) -> None:
        if graph != None:
            self.graph = DiGraph()
            graph_O = json.loads(graph)
            for n in graph_O["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    self.graph.add_node(n["id"], (float(data[0]), float(data[1]), float(data[2])))

            for e in graph_O["Edges"]:
                self.graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))

        if agents != None:
            self.agents = []
            agents_O = json.loads(agents)
            for i in agents_O['Agents']:
                self.agents.append(agent(i['Agent']))

        if pokemons != None:
            self.pokemons.clear()
            pokemons_O = json.loads(pokemons)
            for i in pokemons_O['Pokemons']:
                self.pokemons.append(i['Pokemon'])
            # self.pokemons
            # self.pokemons.append(p)


    def pokemon(self,pokemon):
