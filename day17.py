import time

def style(targetY: "tuple[int, int]"):
  # Assume target y is always negative (is it?)
  return sum(range(1, abs(targetY[0])))

def getMinDomain(targetX: "tuple[int, int]"):
  testMin = 0
  valid = False

  while not valid:
    testMin += 1
    tempSum = 0
    for i in range(testMin, 0, 1 if targetX[0] < 0 else -1):
      tempSum += i

      if (tempSum >= targetX[0]):
        valid = True
        break

  return testMin

def validate(velocityData: "tuple[int, int]", targetData: "list[tuple[int, int]]"):
  pos = list(velocityData)
  curr = list(velocityData)

  while pos[0] <= targetData[0][1] and pos[1] >= targetData[1][0]:
    if (pos[0] >= targetData[0][0] and pos[1] <= targetData[1][1]):
      return True

    if (curr[0] != 0):
      curr[0] += -1 if curr[0] > 0 else 1
    curr[1] -= 1
    
    pos[0] += curr[0]

    pos[1] += curr[1]

  return False

def getAll(targetData: "list[tuple[int, int]]"):
  # Get min and max of y velocity
  # There may be numbers in this range not in the actual range
  # These are the numbers to test with the domain values
  velocityRange = tuple([targetData[1][0], abs(targetData[1][0]) - 1])
  velocityDomain = tuple([getMinDomain(targetData[0]), targetData[0][1]])

  numValid = 0
  for i in range(velocityDomain[0], velocityDomain[1] + 1):
    for j in range(velocityRange[0], velocityRange[1] + 1):
      # if (validate(i, targetData[0], True) and validate(j, targetData[1])):
      # NOTES FOR SESSION #2: validate both x and y at once, instead of individually
      if (validate((i, j), targetData)):
        numValid += 1

  return numValid


if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open("inputFiles/day17.txt", "r") as inputFile:
    inputFromFile = inputFile.read()

  targetData = [tuple(int(j) for j in i.split("..")) for i in inputFromFile.split(": x=")[1].split(", y=")]
  print(f"Part 1: {style(targetData[1])}")
  print(f"Part 2: {getAll(targetData)}")

  print("--- %s seconds ---" % (time.perf_counter() - startTime))