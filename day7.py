import time

def getMedian(inputList: "list[int]"):
  """Get the median value in the input list."""

  copied = inputList.copy()
  copied.sort()
  median = 0

  # Check if length is even
  if (len(inputList) % 2 == 0):
    median = int(sum(copied[int(len(copied) / 2) - 1:int(len(copied) / 2) + 1]) / 2)

  # Check if length is odd
  else:
    median = copied[int(len(copied) / 2 - 0.5)]

  return median

def getAverage(inputList: "list[int]"):
  """Get the average value of the input list, rounded to the nearest integer."""

  return round(sum(inputList) / len(inputList))

def calculateFuel(crabPositions: "list[int]", pos: int):
  """Calculate the overall fuel needed for the crabs to move to a given position."""

  fuelCost = 0
  for i in crabPositions:
    fuelCost += abs(i - pos)

  return fuelCost

def getAlignmentPosWithStep(inputList: "list[int]"):
  """Inefficiently get the correct alignment position."""

  minPos = min(inputList)

  smallest = calculateFuelWithStep(inputList, minPos)
  smallestPos = minPos

  # Brute force from average value
  average = getAverage(inputList)
  for i in range(0, 10):
    calculation = calculateFuelWithStep(inputList, average - i)
    if (calculation < smallest):
      smallest = calculation
      smallestPos = average - i

    calculation = calculateFuelWithStep(inputList, average + i)
    if (calculation < smallest):
      smallest = calculation
      smallestPos = average + i

  return smallestPos

def calculateFuelWithStep(crabPositions: "list[int]", pos: int):
  """Calculate the overall fuel, taking into account the increased unit of fuel for each move."""

  fuelCost = 0
  for i in crabPositions:
    for j in range(1, abs(i - pos) + 1):
      fuelCost += j

  return fuelCost

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day7.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [int(x) for x in inputFromFile.split(',') if x]
  median = getMedian(inputList)
  fuelCost = calculateFuel(inputList, median)
  print(f"Fuel cost: {fuelCost}")

  average = getAlignmentPosWithStep(inputList)
  fuelCostWithStep = calculateFuelWithStep(inputList, average)
  print(f"Fuel cost with step: {fuelCostWithStep}")

  print("--- %s seconds ---" % (time.time() - startTime))