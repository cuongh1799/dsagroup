# Main Application
# Developed in a Java-style architecture

import random
from graph import MapGraph
from exporter import FileExporter
from pathSystem import RoutingEngine

def main():
    TOTAL_NODES = 100 
    
    myMap = MapGraph()
    
    for i in range(TOTAL_NODES):
        myMap.addNode(i)


    for i in range(TOTAL_NODES - 1):
        distance = random.randint(1, 3) 
        times = [max(1, distance * 2 + random.randint(1, 5)) for _ in range(24)] 
        myMap.addEdge(i, i + 1, distance, times) 

        # Create "Shortcuts" (Cross-connections)
        # We make a shortcut every 10 nodes if the jump doesn't exceed the map size
        shortcut_interval = 10
        jump_size = 20
        if i % shortcut_interval == 0 and (i + jump_size) < TOTAL_NODES:
            distance2 = random.randint(5, 15)
            times2 = [max(1, distance2 + random.randint(1, 10)) for _ in range(24)]
            myMap.addEdge(i, i + jump_size, distance2, times2)

    engine = RoutingEngine(myMap)
    exporter = FileExporter()

    source = 0
    destination = TOTAL_NODES - 1 # Set destination to the last node
    hour = 18 # 6:00 PM
    # avoid_nodes = [10, 20]
    # avoid_edges = [(50, 51)]

    # Run Dijkstra for both Distance and Time
    # (Passing None for avoid_nodes and avoid_edges as requested)
    resDist = engine.findPath(source, destination, None, None, "DISTANCE", hour)
    resTime = engine.findPath(source, destination, None, None, "TIME", hour)

    # --- EXPORTING ---
    exporter.exportGraph(myMap, "map_data.txt")
    exporter.exportRouteResults(resDist, resTime, "route_results.txt", source, destination, hour)

    print("\nProcesses finished successfully.")
    print("Files created: 'map_data.txt' and 'route_results.txt'")

if __name__ == "__main__":
    main()