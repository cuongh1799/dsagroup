from models import Edge

class MapGraph:
    def __init__(self):
        self.nodes = []
        self.adjacencyList = {} # Map<Integer, List<Edge>>

    def addNode(self, nodeId):
        if nodeId not in self.nodes:
            self.nodes.append(nodeId)
            self.adjacencyList[nodeId] = []

    def addEdge(self, u, v, distance, timeList):
        edge1 = Edge(u, v, distance, timeList)
        edge2 = Edge(v, u, distance, timeList)
        self.adjacencyList[u].append(edge1)
        self.adjacencyList[v].append(edge2)
