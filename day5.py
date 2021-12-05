import time

class Point:
  def __init__(self):
    self.overlaps = 0

  def getString(self) -> str:
    """Return a printable string for the point."""
    if (self.overlaps > 0):
      return str(self.overlaps)

    return "."

  def addOverlap(self):
    """Add an overlap to the point."""
    self.overlaps += 1

class Graph:
  def __init__(self) -> None:
    graph2DList = []

    for i in range(1001):
      graph2DList.append([Point() for j in range(1001)])

    self.graph2DList = graph2DList

  def getString(self) -> str:
    """Return a printable string for the graph."""
    returnStr = ""
    
    for row in self.graph2DList:
      printStr = [point.getString() for point in row]
      returnStr += "".join(printStr) + "\n"

    return returnStr

  def getPoint(self, x: int, y: int) -> Point:
    return self.graph2DList[y][x]

  def getNumOfMultipleOverlaps(self) -> int:
    """Get the number of points that overlap with at least two lines."""

    count = 0

    for row in self.graph2DList:
      filtered = filter(lambda point: point.overlaps >= 2, row)
      count += len(list(filtered))

    return count

  def addOverlapToPoint(self, x: int, y: int):
    """Add an overlap to a point."""
    self.getPoint(x, y).addOverlap()

  def addLine(self, x1: int, y1: int, x2: int, y2: int, diagonals = False):
    """Add a horizontal, vertical, or diagonal line."""

    if (x1 == x2):
      step = 1
      if (y1 > y2):
        step = -1

      for y in range(y1, y2 + step, step):
        self.addOverlapToPoint(x1, y)

    elif (y1 == y2):
      step = 1
      if (x1 > x2):
        step = -1

      for x in range(x1, x2 + step, step):
        self.addOverlapToPoint(x, y1)
    
    elif (diagonals):
      # Determine direction to iterate in
      deg = (1, -1)

      if (x2 < x1 and y2 < y1):
        # 135 degrees
        deg = (-1, -1)
      elif (x2 < x1 and y2 > y1):
        # 225 degrees
        deg = (-1, 1)
      elif (x2 > x1 and y2 > y1):
        # 315 degrees
        deg = (1, 1)

      xTemp = x1 - deg[0]
      yTemp = y1 - deg[1]

      while (xTemp != x2 and yTemp != y2):
        xTemp += deg[0]
        yTemp += deg[1]
        
        self.addOverlapToPoint(xTemp, yTemp)

def createLines(inputList: "list[str]"):
  """Return a list of tuples that contain information about lines."""

  lines: "list[tuple[list[int]]]" = []

  for line in inputList:
    split = line.split(" -> ")

    point1 = [int(i) for i in split[0].split(",")]
    point2 = [int(i) for i in split[1].split(",")]
    
    lines.append((point1, point2))

  return lines

# Read the input file
if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day5.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [x for x in inputFromFile.split('\n') if x]

  lines = createLines(inputList)

  graph = Graph()
  for line in lines:
    graph.addLine(line[0][0], line[0][1], line[1][0], line[1][1])

  overlaps = graph.getNumOfMultipleOverlaps()
  print(f"Number of overlaps: {overlaps}")

  graphWithDiagonals = Graph()
  for line in lines:
    graphWithDiagonals.addLine(line[0][0], line[0][1], line[1][0], line[1][1], True)

  overlapsWithDiagonals = graphWithDiagonals.getNumOfMultipleOverlaps()
  print(f"Number of overlaps with diagonals: {overlapsWithDiagonals}")

  print("--- %s seconds ---" % (time.time() - startTime))