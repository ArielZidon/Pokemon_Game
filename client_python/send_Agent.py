import math

from GraphAlgo import *
from DiGraph import *
from game import game
from client import Client
epsilon = 0.0000001
pokk = 0

class send_Agent():

    def __init__(self,game:game()) -> None:
        self.game = game
        self.client = Client()
        self.dijkstra = dijkstra(self.game.graph)
        self.inf = float('inf')

    def cmd(self,client:Client):
        for agent in self.game.agents:
            if agent.dest==-1:
                pick = self.pick_pok(agent)
                pick.append(self.game.pokemons[pokk].dest)
                print(pick)
                for i in pick:
                    client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(i) + '}')

    def pick_pok(self,agent):
        min = float('inf')
        G = self.game.graph
        GA = GraphAlgo(G)
        counter = 0

        for pok in self.game.pokemons:
            pick =[]
            counter += 1
            s = GA.shortest_path(agent.src,pok.src)
            if pok.src == agent.src:
                pokk = counter
                return s[1]
            good = s[0]
            if min>good:
                min = good
                pick = s[1]
                pokk = counter
            return pick











    # def cmd(self,client:Client):
    #     for agent in self.game.agents:
    #         G = self.game.graph
    #         GA = GraphAlgo(G)
    #         # pok = self.game.pokemons[0]
    #         agent.dest = self.game.pokemons[1].src
    #         list = GA.shortest_path(agent.src,agent.dest)
    #         list[1].append(self.game.pokemons[1].dest)
    #         # if self.game.pokemons[0]!=pok:
    #         #     agent.dest = self.game.pokemons[0].src
    #         #     list = GA.shortest_path(agent.src, agent.dest)
    #         #     list[1].append(self.game.pokemons[0].dest)
    #
    #         print(list[1])
    #         for i in list[1]:
    #             client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(i) + '}')
    #

