import math as m
from DiGraph import *
from argoments import *
import json

epsilon = 0.00000000001

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




    # def candidateAgent(self, p: pokemon) -> list:
    #     temp = []
    #     for a in self.agents.value():
    #         if len(a.stations) == 0:
    #             temp.append(a.id)
    #     if len(temp) == 0:
    #         temp.append(self.counter % len(self.agents))
    #         self.counter += 1
    #     return temp
    # #
    # def calc(self, a: agent, p: pokemon):
    #     print(p.src, p.dest)
    #     if len(a.stations):
    #         distance = self.shortest_path(a.stations[-1], p.src)
    #     else:
    #         distance = self.shortest_path(a.src, p.src)
    #     time = (distance[0] / a.speed)
    #     return (time, distance)
    #
    # def allocateAgen(self, p: pokemon) -> None:
    #     candidAgents = self.candidateAgent(p)
    #     relevant = float('inf')
    #     candid = path = None
    #     for a in candidAgents:
    #         cal = self.calc(self.agents[a], p)
    #         if cal[0] < relevant:
    #             candid = self.agents[a].id
    #             path = cal[1][1]
    #     path.pop(0)
    #     self.agents[candid].stations += path
    #     self.agents[candid].stations.append(p.dest)
    #     p.agent = candid
    #
    # def allocateAllpokemon(self) -> None:
    #     for p in self.pokemons:
    #         if p.agent == None:
    #             self.allocateAgen(p)
    #
    # def CMD(self, client: Client) -> None:
    #     for a in self.agents.value():
    #         if a.dest == -1 and len(a.stations) != 0:
    #             print(f"a = {a}\n src = {a.src}")
    #             client.choose_next_edge(
    #                 '{"agent_id":' + str(a.id) + ', "next_node_id":' + str(a.stations[0]) + '}')
    #             a.stations.pop(0)