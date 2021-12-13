import time
from operator import itemgetter

class Paper:
  def __init__(self, points: "list[list[int]]"):
    self.points = points

  def pointsAsString(self):
    maxX = max(self.points, key=itemgetter(0))[0]
    maxY = max(self.points, key=itemgetter(1))[1]

    pointsAsStr = ""

    for y in range(maxY + 1):
      for x in range(maxX + 1):
        hasPoint = False

        for point in self.points:
          if (point[0] == x and point[1] == y):
            pointsAsStr += "#"
            hasPoint = True
        
        if (not hasPoint):
          pointsAsStr += " "

      pointsAsStr += "\n"

    return pointsAsStr

  def checkIfDuplicate(self, point: "list[int]"):
    duplicatePoints = [pt for pt in self.points if pt[0] == point[0] and pt[1] == point[1]]

    return len(duplicatePoints) > 1

  def foldAtY(self, y: int):
    pointsToBeFolded = [point for point in self.points if (point[1] > y)]

    for point in pointsToBeFolded.copy():
      point[1] = y - (point[1] - y)

    for point in pointsToBeFolded:
      if (self.checkIfDuplicate(point)):
        self.points.remove(point)

  def foldAtX(self, x: int):
    pointsToBeFolded = [point for point in self.points if (point[0] > x)]

    for point in pointsToBeFolded.copy():
      point[0] = x - (point[0] - x)

    for point in pointsToBeFolded:
      if (self.checkIfDuplicate(point)):
        self.points.remove(point)

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day13.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  splitData = inputFromFile.split("\n\n")
  coordinateData = splitData[0].split("\n")
  foldData = splitData[1].split("\n")

  coordinates = [[int(coord.split(",")[0]), int(coord.split(",")[1])] for coord in coordinateData]

  paper = Paper(coordinates)

  foldDataForLine = foldData[0].split(" ")[2].split("=")
  if (foldDataForLine[0] == "x"):
    paper.foldAtX(int(foldDataForLine[1]))
  else:
    paper.foldAtY(int(foldDataForLine[1]))

  print(f"Number of points after first fold: {len(paper.points)}")

  for line in foldData[1:]:
    foldDataForLine = line.split(" ")[2].split("=")
    if (foldDataForLine[0] == "x"):
      paper.foldAtX(int(foldDataForLine[1]))
    else:
      paper.foldAtY(int(foldDataForLine[1]))

  print("Code formed by points:")
  print(paper.pointsAsString())

  print("--- %s seconds ---" % (time.time() - startTime))