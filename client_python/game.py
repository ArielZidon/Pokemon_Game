import math as m
from DiGraph import *
from argoments import *
import json
from client import Client


epsilon = 0.00000000001
client = Client()

"""
Receiving String from the server and turning 
it into arguments according to the tape
"""

class game:
    def __init__(self) -> None:
        self.graph = DiGraph()
        self.pokemons = []
        self.agents = []

    def up_to_serv(self, pokemons=None, agents=None, graph=None) -> None:

        if graph != None:
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
            pokemons_obj = json.loads(pokemons)
            for i in pokemons_obj['Pokemons']:
                p = pokemon(i['Pokemon'])
                self.pok_pos(p)
                self.pokemons.append(p)

    """
    The function gives each Pokemon the side that is
     on the rise and now we can reach the Pokemon through its side itself
    """

    def pok_pos(self, pok: pokemon) -> None:
        for node1 in self.graph.nodes:
            for node2 in self.graph.nodes:
                dis1 = self.distanceNodes(self.graph.nodes[node1], self.graph.nodes[node2])
                dis2 = (self.distancePokNode(self.graph.nodes[node1], pok) + self.distancePokNode(
                    self.graph.nodes[node2], pok))
                if abs(dis1 - dis2) <= epsilon:
                    src = None
                    dest = None
                    if pok.type == -1:
                        dest = min(node1, node2)
                        src = max(node1, node2)
                    else:
                        dest = max(node1, node2)
                        src = min(node1, node2)

                    if self.isEdge(src, dest):
                        pok.src = src
                        pok.dest = dest
                        # print(src)
                        # print(dest)
                        return
                    return

    def distanceNodes(self, node1: Node, node2: Node):
        dis = m.sqrt(pow(node1.pos[0] - node2.pos[0], 2) + pow(node1.pos[1] - node2.pos[1], 2))
        return dis

    def distancePokNode(self, node1: Node, pok: pokemon):
        dis = m.sqrt(pow(node1.pos[0] - pok.pos[0], 2) + pow(node1.pos[1] - pok.pos[1], 2))
        return dis

    def isEdge(self, src, dest) -> bool:
        return (src, dest) in self.graph.edges

