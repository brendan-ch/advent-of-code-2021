import time

class Point:
  def __init__(self, coords: "tuple[int]", height: int):
    self.resolved = False
    self.coords = coords

    self.height = height

class Basin:
  def __init__(self, startingPoint: "tuple[int]", startingHeight: int):
    self.points = [Point(startingPoint, startingHeight)]

  def getResolvedStatus(self):
    """Return true if all points are resolved."""
    resolved = True

    for point in self.points:
      if (not point.resolved):
        resolved = False
        break

    return resolved

  def checkIfCoordExists(self, coords: "tuple[int]"):
    """Return true if a coordinate exists in the points list."""

    pointsWithCoords = [point for point in self.points if point.coords == coords]

    return len(pointsWithCoords) > 0

  def checkPoints(self, heightMap: "list[list[int]]"):
    """Mark points as resolved and create new ones."""
    # Copy points
    copiedPoints = self.points.copy()

    for point in copiedPoints:
      if (point.resolved):
        continue

      # Check four locations, create new points
      # Top
      if (point.coords[1] > 0):
        new = heightMap[point.coords[1] - 1][point.coords[0]]
        if (new < 9 and not self.checkIfCoordExists((point.coords[0], point.coords[1] - 1))):
          self.points.append(Point((point.coords[0], point.coords[1] - 1), new))

      # Bottom
      if (point.coords[1] < len(heightMap) - 1):
        new = heightMap[point.coords[1] + 1][point.coords[0]]
        if (new < 9 and not self.checkIfCoordExists((point.coords[0], point.coords[1] + 1))):
          self.points.append(Point((point.coords[0], point.coords[1] + 1), new))

      # Left
      if (point.coords[0] > 0):
        new = heightMap[point.coords[1]][point.coords[0] - 1]
        if (new < 9 and not self.checkIfCoordExists((point.coords[0] - 1, point.coords[1]))):
          self.points.append(Point((point.coords[0] - 1, point.coords[1]), new))

      # Right
      if (point.coords[0] < len(heightMap[point.coords[1]]) - 1):
        new = heightMap[point.coords[1]][point.coords[0] + 1]
        if (new < 9 and not self.checkIfCoordExists((point.coords[0] + 1, point.coords[1]))):
          self.points.append(Point((point.coords[0] + 1, point.coords[1]), new))

      point.resolved = True

def getHeightMap(inputList: "list[str]"):
  """Get all the points represented as a 2D list."""

  points: "list[list[int]]" = []

  for line in inputList:
    points.append([int(x) for x in line])

  return points

def getLowPoints(points: "list[list[int]]"):
  """Get a list of all the low points."""

  y = 0
  x = 0

  lowPoints: "list[int]" = []

  while (y < len(points)):
    while (x < len(points[y])):
      # Check four locations
      if not (
        (y > 0 and points[y - 1][x] <= points[y][x])
        or (y < len(points) - 1 and points[y + 1][x] <= points[y][x])
        or (x > 0 and points[y][x - 1] <= points[y][x])
        or (x < len(points[y]) - 1 and points[y][x + 1] <= points[y][x])
      ):
        lowPoints.append(points[y][x])

      x += 1
    x = 0
    y += 1

  return lowPoints

def getBasinSizes(points: "list[list[int]]"):
  """Get a list of basin sizes."""

  x = 0
  y = 0

  basins: "list[Basin]" = []
  basinSizes = []

  while (y < len(points)):
    while (x < len(points[y])):
      if not (
        (y > 0 and points[y - 1][x] <= points[y][x])
        or (y < len(points) - 1 and points[y + 1][x] <= points[y][x])
        or (x > 0 and points[y][x - 1] <= points[y][x])
        or (x < len(points[y]) - 1 and points[y][x + 1] <= points[y][x])
      ):
        basins.append(Basin((x, y), points[y][x]))
      
      x += 1
    x = 0
    y += 1

  for basin in basins:
    while (not basin.getResolvedStatus()):
      basin.checkPoints(points)
    
    basinSizes.append(len(basin.points))

  basinSizes.sort(reverse=True)

  return basinSizes

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day9.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split('\n') if x]

  pointsMap = getHeightMap(inputList)
  lowPoints = getLowPoints(pointsMap)
  riskLevels = [i + 1 for i in lowPoints]
  print(f"Sum of risk levels: {sum(riskLevels)}")

  basinSizes = getBasinSizes(pointsMap)
  print(f"Product of three largest basin sizes: {basinSizes[0] * basinSizes[1] * basinSizes[2]}")

  print("--- %s seconds ---" % (time.time() - startTime))