import time

class Point:
  def __init__(self, weight: int = 1):
    # Set of pointers
    self.linked: "set[Point]" = set()
    self.weight = weight

  def addLinked(self, vertexToLink: "Point"):
    if (vertexToLink not in self.linked):
      self.linked.add(vertexToLink)

class PointWrapper:
  """Point wrapper for use in the priority queue."""
  def __init__(self, point: Point, previous: Point, dist: int):
    self.point = point
    self.dist = dist
    self.previous = previous

class Graph:
  def __init__(self, points):
    self.graph: "list[Point]" = points

  def printGraph(self):
    for point in self.graph:
      print(f"{point}: {point.linked}")

  def dijkstra(self):
    startIndex = 0
    # Store final distance from start
    # PointWrapper stores distance in queue, which is compared to final distance
    # in while loop
    # If new distance is lower than final distance, replace with new distance
    pathValues = [0]
    pathValues.extend([float('inf')] * (len(self.graph) - 1))

    resolved: "list[Point]" = []
    # currentVertex = startIndex

    # Track adjacency (points that need to be "served")
    # Priority queue based on distance from start
    queue: "list[PointWrapper]" = [PointWrapper(self.graph[startIndex], self.graph[startIndex], 0)]
    
    while (len(resolved) < len(self.graph)):
      # Get point with minimum distance value (priority)
      point = min(queue, key=lambda item: item.dist)

      if (point.point not in resolved):
        resolved.append(point.point)

      queue.remove(point)

      for newPoint in point.point.linked:
        if (newPoint not in resolved):
          existing = [item for item in queue if item.point == newPoint and item.previous == point.point]
          if (len(existing) == 0):
            queue.append(PointWrapper(newPoint, point.point, point.dist + newPoint.weight))
          
            # Compare with value in pathValues
            index = self.graph.index(newPoint)
            if (pathValues[index] > point.dist + newPoint.weight):
              pathValues[index] = point.dist + newPoint.weight

    return pathValues[-1]


if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open('inputFiles/day15.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  points: "list[Point]" = []
  pointList = [[Point(int(i)) for i in row] for row in inputFromFile.split('\n')]
  for i in range(len(pointList)): # row
    for j in range(len(pointList[i])): # column
      # pointsToLink = []
      
      if (i > 0):
        pointList[i][j].addLinked(pointList[i - 1][j])

      if (i < len(pointList) - 1):
        pointList[i][j].addLinked(pointList[i + 1][j])

      if (j > 0):
        pointList[i][j].addLinked(pointList[i][j - 1])

      if (j < len(pointList[i]) - 1):
        pointList[i][j].addLinked(pointList[i][j + 1])

      points.append(pointList[i][j])

  graph = Graph(points)
  print(f"Lowest total risk for part 1: {graph.dijkstra()}")


  print("--- %s seconds ---" % (time.perf_counter() - startTime))