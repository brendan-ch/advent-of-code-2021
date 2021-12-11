import time
import copy

def checkIfSynchronized(octopusMap: "list[list[int]]"):
  """Check if every single value is a 0."""

  for row in octopusMap:
    for octopus in row:
      if (octopus != 0):
        return False

  return True

def simulateStep(octopusMap: "list[list[int]]"):
  """Simulate a step *in place* and return the number of flashes after the step."""

  for y in range(len(octopusMap)):
    for x in range(len(octopusMap[0])):
      octopusMap[y][x] += 1

  resolvedCoords: "list[tuple[int]]" = []
  numFlashes = 0

  # Check which ones are greater than 9
  while True:
    hasGreaterThanNine = False

    for y in range(len(octopusMap)):
      for x in range(len(octopusMap[0])):
        if (octopusMap[y][x] > 9):
          numFlashes += 1
          hasGreaterThanNine = True
          # Increase value of octopi adjacent to octopus

          for yTemp in range(y - 1 if y > 0 else y, y + 2 if y < len(octopusMap) - 1 else y + 1):
            for xTemp in range(x - 1 if x > 0 else x, x + 2 if x < len(octopusMap[y]) - 1 else x + 1):
              if (resolvedCoords.count((xTemp, yTemp)) == 0):
                # Increase value
                octopusMap[yTemp][xTemp] += 1



          octopusMap[y][x] = 0
          resolvedCoords.append((x, y))

    if (not hasGreaterThanNine):
      return numFlashes

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day11.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split('\n') if x]

  octopusMap = [[int(x) for x in line] for line in inputList]
  octopusMapCopy = copy.deepcopy(octopusMap)
  numSteps = 100
  numFlashes = 0
  for i in range(numSteps):
    numFlashes += simulateStep(octopusMap)

  print(f"Number of flashes in 100 steps: {numFlashes}")

  numStepsUntilSynced = 0

  while (not checkIfSynchronized(octopusMapCopy)):
    simulateStep(octopusMapCopy)

    numStepsUntilSynced += 1

  print(f"Number of steps until synchronized: {numStepsUntilSynced}")


  print("--- %s seconds ---" % (time.time() - startTime))