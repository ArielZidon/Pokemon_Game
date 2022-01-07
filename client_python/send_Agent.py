import math
from GraphAlgo import *
from DiGraph import *
from game import game
from client import Client
import time
epsilon = 0.0000001
pokk = 0

class send_Agent():

    def __init__(self,game:game()) -> None:
        self.game = game
        self.client = Client()
        self.dijkstra = dijkstra(self.game.graph)
        self.inf = float('inf')
        self.fast_move = time.sleep(0.035)
        self.low_move = time.sleep(0.1)


    def cmd_solo(self,client:Client,t):
        pick = []

        for agent in self.game.agents:
            if agent.dest==-1:
                pick = self.pick_pok(agent)
                for i in pick:
                    client.choose_next_edge('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(pick[1]) + '}')

        # ///////////////stop singel//////////////////////////////
        if t == 1:
            if len(pick) <= 2:
                if self.game.agents[0].speed >= 3:
                    time.sleep(0.03)
                else:
                    time.sleep(0.03)
            else:
                if self.game.agents[0].speed <= 3:
                    time.sleep(0.6)
                else:
                    time.sleep(0.05)

        else:
            if len(pick) <= 2:
                if self.game.agents[0].speed >= 2:
                    time.sleep(0.03)
                else:
                    time.sleep(0.03)
            else:
                if self.game.agents[0].speed <= 2:
                    time.sleep(0.6)
                else:
                    time.sleep(0.06)
    # //////////////////////////////////////////////////////////////

    def pick_pok(self,agent):
        G = self.game.graph
        GA = GraphAlgo(G)
        pick = []
        res = []
        min = 0
        i = 0
        max = 0
        p = None
        for pok in self.game.pokemons:
            max+=1

        for pok in self.game.pokemons:
            if pok.mode == 0:

                if pok.src == None or agent.src == None:
                    pok.src = 7
                    pok.dest = 6

                s = GA.shortest_path(agent.src,pok.src)
                pick = s[0],s[1],pok.value

                w = (pok.value/(s[0]+1))

                if min<w:
                    min = w
                    res = pick[1]
                    p = pok
                    i+=1
                    if i<max:
                        continue
        res.append(p.dest)
        return res




    # ////////////////////////////////////////////more then one/////////////////////////////////////////////////////////

    def cmd_group(self, client: Client, t):

        for pok in self.game.pokemons:
            self.pick_age(pok,client,t)
        time.sleep(0.025)


    def pick_age(self, pokemon,client,t):
        if pokemon.mode == 0:
            G = self.game.graph
            GA = GraphAlgo(G)
            pick = []
            res = []
            min = 0
            i = 0
            max = 0
            a = None

            for AG in self.game.agents:
                max += 1

            for agent in self.game.agents:
                    s = GA.shortest_path(agent.src, pokemon.src)
                    pick = s[0], s[1], pokemon.value

                    w = (pokemon.value / (s[0] + 1))*agent.speed

                    if min < w:
                        min = w
                        res = pick[1]
                        a = agent
                        res[0] = a.id
                        res.append(pokemon.dest)
                        i += 1
                        if i < max:
                            continue
            client.choose_next_edge(
                '{"agent_id":' + str(res[0]) + ', "next_node_id":' + str(res[1]) + '}')

            # for agent in self.game.agents:
            #     if agent.dest == -1:
            #         client.choose_next_edge(
            #             '{"agent_id":' + str(res[0]) + ', "next_node_id":' + str(res[1]) + '}')





  # j = 0
  #       for pok in self.game.pokemons:
  #           if p.pos == pok.pos:
  #               pok.mode = 1
  #           i += 1
  #           if i < 4:
  #               continue
  #       res.append(p.dest)


# age = None
# speed = 0
# min = 0
# for agent in self.game.agents:
#     speed = agent.speed
#     if speed > min:
#         min = speed
#         age = agent

# if len(pick) <= 2:
#     if age.speed >= 3:
#         time.sleep(0.028)
#     else:
#         time.sleep(0.028)
# else:
#     if age.speed <= 3:
#         time.sleep(0.028)
#     else:
#         time.sleep(0.028)