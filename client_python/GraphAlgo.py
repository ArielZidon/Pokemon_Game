"""
Class GraphAlgo
In this class we have algorithms of a graph
Used to do operations on the graph and to get more information about the graph (e.g. shortest path)
"""
from DiGraph import DiGraph
import json


class GraphAlgo():
    # constructor
    def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph
        self.dijkstra = dijkstra(graph)
        self.inf = float('inf')

    # getter for the graph
    def get_graph(self) -> DiGraph():
        return self.graph

    # function to find the shortest path from a given node to another given node
    # in order to do that we use dijkstra algorithm
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.getdijk(id1)
        self.dijkstra.addPath(id2)
        start = self.dijkstra.D[id2]
        end = self.dijkstra.roads[id2]
        return (start,end)

    # function to find the center of the graph
    # in order to find it we use dijkstra algorithm
    def centerPoint(self) -> (int, float):
        try:
            res = (0, self.inf)
            for i in self.graph.nodes:
                self.getdijk(i)
                rD = (i, max(self.dijkstra.D.values()))
                if res[1] > rD[1]:
                    res = rD
            return res
        except:
            return (0,self.inf)

    # ToString
    def __repr__(self) -> str:
        return f'{self.graph}'

    # performing dijkstra algorithm on a given source node
    def getdijk(self, src: int) -> bool:
        if src == self.dijkstra.src and self.graph.mc == self.dijkstra.mc:
            return False
        else:
            self.dijkstra.src = src
            self.dijkstra.MC = self.graph.mc
            self.dijkstra.goForIt()
            return True

    # load a graph from json file
    def load_from_json(self, file_name: str) -> bool:
        try:
            dict = {}
            graph_res = self.graph
            with open(file_name, "r") as f:
                dict = json.load(f)

            for n in dict["Nodes"]:
                if "pos" in n:
                    data = n["pos"].split(',')
                    graph_res.add_node(n["id"], (data[0], data[1], data[2]))
                else:
                    graph_res.add_node(n["id"])

            for e in dict["Edges"]:
                graph_res.add_edge(e["src"], e["dest"], e["w"])

        except IOError as e:
            print(e)
            return False
        self.graph = graph_res
        return True


"""
Class dijkstra:
represents the dijkstra algorithm
"""
class dijkstra:
    # constructor
    def __init__(self, graph: DiGraph):
        self.src = 0
        self.graph = graph
        self.mc = 0
        self.inf = float('inf')

        # hashmaps
        self.roads = {}
        self.paps = {}
        self.D = {}

    def goForIt(self):
        var = []
        self.initshate(self.paps, var)
        while len(var) != 0:
            small = self.theSmallest(var)
            if small == -self.inf:
                return
            for i in self.graph.all_out_edges_of_node(small):
                self.updating(small,i)

    def updating(self, s: int, d: int):
        updatedDistance = self.D[s] + self.graph.edges[(s, d)]
        if updatedDistance >= self.D[d]:
            return
        else:
            self.D[d] = updatedDistance
            self.paps[d] = s

    def initshate(self, fathers: dict, listPerNode: list):
        for i in self.graph.nodes.keys():
            if i != self.src:
                self.D[i] = self.inf
                fathers[i] = self.inf
                listPerNode.append(i)
                self.roads[i] = []
        fathers[self.src] = self.src
        self.D[self.src] = 0.0
        self.roads[self.src] = []
        listPerNode.append(self.src)

    def addPath(self, next: int):
        if len(self.roads[next]) != 0:
            return
        self.roads[next] = []
        if next == self.src:
            self.roads[next].append(next)
            return
        dad = self.paps[next]
        if dad == self.inf:
            return
        if dad in self.roads:
            self.addPath(dad)
        self.roads[next].extend(self.roads[dad])
        self.roads[next].append(next)

    def theSmallest(self, p: list) -> int:
        M = self.inf
        ans = -self.inf
        for i in p:
            if M > self.D[i]:
                ans = i
                M = self.D[i]
        if ans != -self.inf:
            p.remove(ans)
        return ans