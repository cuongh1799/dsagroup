# Map Routing System with File Export
# Developed in a Java-style architecture

import random
from graph import MapGraph
from exporter import FileExporter
from pathSystem import RoutingEngine

def main():
    myMap = MapGraph()
    # Generate 2000 nodes
    for i in range(2000):
        myMap.addNode(i)

    # Generate edges
    for i in range(1999):
        distance = random.randint(10, 50) # generate random distance 
        times = [max(1, distance + random.randint(-5, 15)) for _ in range(24)] # populated the time
        myMap.addEdge(i, i + 1, distance, times) 
        if i % 20 == 0 and i + 100 < 2000:
            distance2 = random.randint(100, 300)
            times2 = [max(1, distance2 + random.randint(-10, 40)) for _ in range(24)]
            myMap.addEdge(i, i + 100, distance2, times2)

    engine = RoutingEngine(myMap)
    exporter = FileExporter()

    # Query
    source, destination, hour = 0, 1250, 18
    avoid_nodes = [10, 20]
    avoid_edges = [(50, 51)]

    # Run Algorithms
    resDist = engine.findPath(source, destination, avoid_nodes, avoid_edges, "DISTANCE", hour)
    resTime = engine.findPath(source, destination, avoid_nodes, avoid_edges, "TIME", hour)

    # Export to Files
    exporter.exportGraph(myMap, "map_data.txt")
    exporter.exportRouteResults(resDist, resTime, "route_results.txt", source, destination, hour)

    print("\nProcesses finished. Check 'map_data.txt' and 'route_results.txt'.")

if __name__ == "__main__":
    main()
