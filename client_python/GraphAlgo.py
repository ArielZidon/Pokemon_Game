from DiGraph import DiGraph

class GraphAlgo():
    def __init__(self,graph=DiGraph()) -> None:
        self.graph = graph
        self.dijkstra = dijkstra(graph)
        self.inf = float('inf')

    def get_graph(self) -> DiGraph():
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.getdijk(id1)
        self.dijkstra.addPath(id2)
        start = self.dijkstra.D[id2]
        end = self.dijkstra.roads[id2]
        return (start,end)


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


    def __repr__(self) -> str:
        return f'{self.graph}'


    def getdijk(self, src: int) -> bool:
        if src == self.dijkstra.src and self.graph.mc == self.dijkstra.mc:
            return False
        else:
            self.dijkstra.src = src
            self.dijkstra.MC = self.graph.mc
            self.dijkstra.goForIt()
            return True





class dijkstra:

    def __init__(self,graph:DiGraph):
        self.src = 0
        self.graph = graph
        self.mc = 0
        self.inf = float('inf')

    #hashmaps
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


    def initshate(self,fathers: dict, listPerNode: list):
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







