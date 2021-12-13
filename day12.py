import time

class Point:
  def __init__(self, identifier: str) -> None:
    self.id = identifier
    self.pointers: "list[Point]" = []
    self.isSmallCave = identifier.upper() != identifier

  def setPointer(self, point: "Point"):
    self.pointers.append(point)

def linkCaves(inputList: "list[str]"):
  """Link the points together and return the starting point."""

  # Create the caves first
  # Store caves identifiers already created
  createdCaves: "list[Point]" = [Point("start")]

  for line in inputList:
    for caveStr in line.split("-"):
      matchingCaves = [cave for cave in createdCaves if cave.id == caveStr]

      if (len(matchingCaves) == 0):
        createdCaves.append(Point(caveStr))

  # Link caves together
  for line in inputList:
    splitLine = line.split("-")

    for i in range(len(splitLine)):
      matchingCaves = [cave for cave in createdCaves if cave.id == splitLine[i]]
      linkedCaves = [cave for cave in createdCaves if cave.id == splitLine[i - 1]]

      if (len(matchingCaves) == 1 and len(linkedCaves) == 1):
        matchingCaves[0].setPointer(linkedCaves[0])

  return createdCaves[0]

def navigateToNextPart2(currentPoint: Point, path: "list[Point]", allPaths: "list[list[Point]]"):
  """Navigate to the next point, using the updated set of rules."""

  path.append(currentPoint)

  # Get unique points by converting to set
  uniquePoints = set(path)

  countsOfSmallCaves = [path.count(point) for point in uniquePoints if point.isSmallCave]
  
  if (currentPoint.id == "end"):
    allPaths.append(path)
    return

  allowTraverseToSmallCave = countsOfSmallCaves.count(2) == 0
  for point in currentPoint.pointers:
    if (
      point.id != "start" 
      and (
        not point.isSmallCave
        or (
          point.isSmallCave
          and ((path.count(point) == 1 and allowTraverseToSmallCave) or path.count(point) == 0)
        )
      )
    ):
      navigateToNextPart2(point, path.copy(), allPaths)

def navigateToNext(currentPoint: Point, path: "list[Point]", allPaths: "list[list[Point]]"):
  """Navigate to the next point."""

  path.append(currentPoint)
  if (currentPoint.id == "end"):
    allPaths.append(path)
    return

  # Filter points here which haven't been traversed yet
  for point in currentPoint.pointers:
    # Check in path list for times traversed, instead of 
    # storing value in each point
    # Check if large or small cave

    # Use copy of path list when recursing

    # Append list to allPaths when done recursing

    if (point.id != "start" and ((not point.isSmallCave) or (point.isSmallCave and path.count(point) == 0))):
      navigateToNext(point, path.copy(), allPaths)

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day12.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split('\n') if x]

  startingPoint = linkCaves(inputList)

  allPaths = []
  navigateToNext(startingPoint, [], allPaths)

  print(f"Number of paths: {len(allPaths)}")

  allPaths = []
  navigateToNextPart2(startingPoint, [], allPaths)

  print(f"Number of paths for part 2: {len(allPaths)}")

  print("--- %s seconds ---" % (time.time() - startTime))