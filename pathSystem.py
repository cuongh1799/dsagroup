from models import PathResult

class RoutingEngine:
    def __init__(self, graph):
        self.graph = graph

    def findPath(self, startNode, endNode, avoidNodes, avoidEdges, mode, hour):
        infinity = 999999999.9
        distances = {}
        previousNodes = {}
        unvisited = []

        # Initialize tracking structures for Dijkstra's algorithm.
        # Distances are set to infinity as they are currently unknown,
        # and all nodes are marked as unvisited initially.
        for node in self.graph.nodes:
            distances[node] = infinity
            previousNodes[node] = None
            unvisited.append(node) # append everything

        # Validate that the start node exists in our graph.
        # Initialize the start node distance to 0 so the algorithm selects it first.
        if startNode not in distances: return None
        distances[startNode] = 0.0

        # Greedily search through unvisited nodes.
        # It needs to process nodes starting with the currently known shortest path.
        while len(unvisited) > 0: # if there is unvisited node
            currentNode = unvisited[0]
            for node in unvisited:
                if distances[node] < distances[currentNode]:
                    currentNode = node

            # if found endnode
            if currentNode == endNode or distances[currentNode] == infinity:
                break
            
            # mark it as visted already
            unvisited.remove(currentNode)

            # If the current node is in the list of nodes to avoid, skip processing it
            if avoidNodes and currentNode in avoidNodes:
                continue

            # Iterate over all adjacent edges (neighbors) of the current node
            for edge in self.graph.adjacencyList[currentNode]:
                neighbor = edge.destination
                
                # Check if this specific edge is in the list of edges to avoid (in either direction)
                shouldAvoid = False
                if avoidEdges:
                    for forbidden in avoidEdges:
                        # We check both directions (source->dest and dest->source) because the graph is undirected (two-way roads).
                        # We use a 'shouldAvoid' flag and 'break' instead of an immediate 'continue' here, 
                        # because 'continue' would only skip to the next item in the inner 'avoidEdges' loop, 
                        # rather than skipping the current edge in the outer loop.
                        if (forbidden[0] == edge.source and forbidden[1] == edge.destination) or \
                           (forbidden[1] == edge.source and forbidden[0] == edge.destination):
                            shouldAvoid = True
                            break
                
                # Skip to the next edge if it's forbidden or if the neighbor has already been visited
                if shouldAvoid or (neighbor not in unvisited):
                    continue

                # if mode is distance, choose distance data of edge
                # if mode is time, choose timeList
                weight = float(edge.distance) if mode == "DISTANCE" else float(edge.timeList[hour])

                # Dijkstra's relaxation step: Calculate new distance to neighbor
                # If the new path is shorter than the currently known path, update distance and previous node
                newDist = distances[currentNode] + weight
                if newDist < distances[neighbor]:
                    distances[neighbor] = newDist
                    previousNodes[neighbor] = currentNode

        # Path reconstruction
        path = []
        temp = endNode
        if distances[endNode] == infinity: return None

        # Walk back the nodes
        while temp is not None:
            path.insert(0, temp)
            temp = previousNodes[temp]

        # Calculate totals
        finalD, finalT = 0.0, 0.0
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            for e in self.graph.adjacencyList[u]:
                if e.destination == v:
                    finalD += e.distance
                    finalT += e.timeList[hour]
                    break

        return PathResult(path, finalD, finalT)
