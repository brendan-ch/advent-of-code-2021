import time

class Point:
  def __init__(self, weight: int = 1):
    # Set of pointers
    self.linked: "set[Point]" = set()
    self.weight = weight

  def addLinked(self, vertexToLink: "Point"):
    if (vertexToLink not in self.linked):
      self.linked.add(vertexToLink)

  def incrementWeight(self, amount: int):
    self.weight += amount
    if (self.weight > 9):
      self.weight -= 9

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
    result = 0

    resolved: "set[Point]" = set()

    # Track adjacency (points that need to be "served")
    # Priority queue based on distance from start
    queue: "set[PointWrapper]" = set([PointWrapper(self.graph[startIndex], self.graph[startIndex], 0)])
    
    while (len(resolved) < len(self.graph)):
      # Get point with minimum distance value (priority)
      point = min(queue, key=lambda item: item.dist)

      for newPoint in [pt for pt in point.point.linked if pt not in resolved]:
        newDist = point.dist + newPoint.weight
        
        # Append to queue
        queue.add(PointWrapper(newPoint, point.point, newDist))

        # Add new point to resolved now, so it doesn't get added again to queue later
        resolved.add(newPoint)

        # # Compare with value in pathValues
        index = self.graph.index(newPoint)
        if (index == len(self.graph) - 1):
          result = newDist
          break

      queue.remove(point)

    return result

  @staticmethod
  def linkPoints(pointList: "list[list[Point]]"):
    """Link the points inside the pointList, and return a list of all points."""
    points: "list[Point]" = []
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

    return points

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open('inputFiles/day15.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  pointList = [[Point(int(i)) for i in row] for row in inputFromFile.split('\n')]
  points = Graph.linkPoints(pointList)

  graph = Graph(points)
  print(f"Lowest total risk for part 1: {graph.dijkstra()}")

  # Reset point list
  pointList = [[Point(int(i)) for i in row] for row in inputFromFile.split('\n')]

  # Extend pointList for part 2
  # Extend horizontally
  for row in range(len(pointList)):
    rowCopy = pointList[row].copy()

    for i in range(1, 5):
      copied = [Point(item.weight) for item in rowCopy]
      for item in copied:
        item.incrementWeight(i)

      pointList[row].extend(copied)

  # Extend vertically
  originalLength = len(pointList)
  i = 1
  while (len(pointList) < originalLength * 5):
    for row in range(originalLength):
      copied = [Point(item.weight) for item in pointList[row]]
      for item in copied:
        item.incrementWeight(i)

      pointList.append(copied)

    i += 1

  # Re-link points
  points = Graph.linkPoints(pointList)

  graph = Graph(points)

  print(f"Lowest total risk for part 2: {graph.dijkstra()}")
  print("--- %s seconds ---" % (time.perf_counter() - startTime))