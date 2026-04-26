class Edge:
    def __init__(self, source, destination, distance, timeList):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.timeList = timeList

class PathResult:
    def __init__(self, nodeSequence, totalDistance, totalTime):
        self.nodeSequence = nodeSequence
        self.totalDistance = totalDistance
        self.totalTime = totalTime
