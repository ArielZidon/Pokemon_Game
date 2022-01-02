from DiGraph import DiGraph
from  GraphAlgo import GraphAlgo
from argoments import *
import json
class game():

    def __init__(self) -> None:
        self.pockemons = []
        self.agents =[]
        self.graph = DiGraph()
        self.graphAlgo =GraphAlgo()

    def builder(self,pokemons = None,agents = None,graph =None):
        if pokemons!=None:
            self.pokemons = pokemons
            pokemons_O = json.loads(pokemons)
            for i in pokemons_O['Pokemons']:
                self.pockemons.append(pokemon(i['Pokemon']))

        if agents!=None:
            self.agents = []
            agents_O = json.loads(agents)
            for i in agents_O['Agents']:
                self.agents.append(agent(i['Agent']))

        if graph!=None:
            self.graph = DiGraph()
            graph_O = json.loads(graph)
            for n in graph_O["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    self.graph.add_node(n["id"], (data[0], data[1], data[2]))
                else:
                    self.graph.add_node(n["id"])

            for e in graph_O["Edges"]:
                self.graph.add_edge(e["src"], e["dest"], e["w"])


