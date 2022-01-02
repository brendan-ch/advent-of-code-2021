import time
from copy import deepcopy

def getNextCoord(dataset: "list", i: int):
  if (i + 1 >= len(dataset)):
    return 0
  
  return i + 1

def simulateStep(cucumberList: "list[list[str]]"):
  # Move east-facing
  for row in range(len(cucumberList)):
    newCopy = cucumberList[row].copy()

    for i in range(len(cucumberList[row])):
      nextCoord = getNextCoord(newCopy, i)
      if (newCopy[i] == '>' and newCopy[nextCoord] == '.'):
        cucumberList[row][nextCoord] = '>'
        cucumberList[row][i] = '.'

  # Move south-facing
  newCopy = deepcopy(cucumberList)
  for row in range(len(cucumberList)):

    for i in range(len(cucumberList[row])):
      nextCoord = getNextCoord(newCopy, row)
      if (newCopy[row][i] == 'v' and newCopy[nextCoord][i] == '.'):
        cucumberList[nextCoord][i] = 'v'
        cucumberList[row][i] = '.'

def printList(cucumberList: "list[list[str]]"):
  for i in cucumberList:
    line = ''

    for j in i:
      line += j

    print(line)

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open("inputFiles/day25.txt", "r") as inputFile:
    inputFromFile = inputFile.read()

  cucumberList = [[j for j in i] for i in inputFromFile.split('\n')]
  last = deepcopy(cucumberList)

  simulateStep(cucumberList)
  i = 1

  while (last != cucumberList):
    last = deepcopy(cucumberList)
    simulateStep(cucumberList)

    i += 1

  print(f"Number of steps until no movement: {i}")

  print("--- %s seconds ---" % (time.perf_counter() - startTime))