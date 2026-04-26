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
        d = random.randint(10, 50)
        t = [max(1, d + random.randint(-5, 15)) for _ in range(24)]
        myMap.addEdge(i, i + 1, d, t)
        if i % 20 == 0 and i + 100 < 2000:
            d2 = random.randint(100, 300)
            t2 = [max(1, d2 + random.randint(-10, 40)) for _ in range(24)]
            myMap.addEdge(i, i + 100, d2, t2)

    engine = RoutingEngine(myMap)
    exporter = FileExporter()

    # Query
    src, dest, hr = 0, 1250, 18
    avoid_n = [10, 20]
    avoid_e = [(50, 51)]

    # Run Algorithms
    resDist = engine.findPath(src, dest, avoid_n, avoid_e, "DISTANCE", hr)
    resTime = engine.findPath(src, dest, avoid_n, avoid_e, "TIME", hr)

    # Export to Files
    exporter.exportGraph(myMap, "map_data.txt")
    exporter.exportRouteResults(resDist, resTime, "route_results.txt", src, dest, hr)

    print("\nProcesses finished. Check 'map_data.txt' and 'route_results.txt'.")

if __name__ == "__main__":
    main()
