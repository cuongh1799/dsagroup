# p/s this whole thing was ai gen because lazy

class FileExporter:
    """This class handles exporting data to TXT files (Similar to Java File IO)"""
    
    def exportGraph(self, graph, fileName):
        print(f"Exporting graph to {fileName}...")
        file = open(fileName, "w")
        file.write("--- MAP GRAPH DATA ---\n")
        file.write(f"Total Nodes: {len(graph.nodes)}\n")
        file.write("Format: Source -> Destination | Distance | [24h Travel Times]\n\n")
        
        for node in graph.nodes:
            for edge in graph.adjacencyList[node]:
                # Only print u -> v where u < v to avoid duplicates in undirected graph
                if edge.source < edge.destination:
                    line = f"Edge: {edge.source} -> {edge.destination} | Dist: {edge.distance} | Times: {edge.timeList}\n"
                    file.write(line)
        file.close()
        print("Graph export complete.")

    def exportRouteResults(self, resDist, resTime, fileName, source, dest, hour):
        print(f"Exporting results to {fileName}...")
        file = open(fileName, "w")
        file.write("--- ROUTE QUERY RESULTS ---\n")
        file.write(f"Query: From {source} to {dest} at Hour {hour}:00\n\n")

        # Write Distance Results
        file.write("[OPTIMIZED BY DISTANCE]\n")
        if resDist:
            file.write(f"Total Distance: {resDist.totalDistance}\n")
            file.write(f"Total Time: {resDist.totalTime}\n")
            file.write(f"Path: {resDist.nodeSequence}\n\n")
        else:
            file.write("No path found.\n\n")

        # Write Time Results
        file.write("[OPTIMIZED BY TIME]\n")
        if resTime:
            file.write(f"Total Distance: {resTime.totalDistance}\n")
            file.write(f"Total Time: {resTime.totalTime}\n")
            file.write(f"Path: {resTime.nodeSequence}\n")
        else:
            file.write("No path found.\n")
            
        file.close()
        print("Results export complete.")
