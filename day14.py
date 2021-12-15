import time
import copy

def getLetterCounts(stringInfo: "dict[str, dict[str, any]]"):
  # Get unique letters
  allLetters = ""
  for key in stringInfo:
    allLetters += key

  uniqueLetters = set(allLetters)
  letterCounter = {}
  for letter in uniqueLetters:
    letterCounter[letter] = 0

  for key in stringInfo:
    letterCounter[key[:1]] += stringInfo[key]["numCount"]
    letterCounter[key[1:]] += stringInfo[key]["numCount"]

  for key in letterCounter:
    letterCounter[key] = int(letterCounter[key] / 2 + 0.5)

  return max(letterCounter.values()) - min(letterCounter.values())

def insertPairsEfficient(stringInfo: "dict[str, dict[str, any]]"):
  """Return a new stringInfo dictionary with the inserted pairs."""
  newStringInfo = copy.deepcopy(stringInfo)
  
  for key in stringInfo:
    numInsertions = stringInfo[key]["numCount"]

    # Perform insertion
    newStringInfo[key[:1] + stringInfo[key]["charToInsert"]]["numCount"] += numInsertions
    newStringInfo[stringInfo[key]["charToInsert"] + key[1:]]["numCount"] += numInsertions
    newStringInfo[key]["numCount"] -= numInsertions

  return newStringInfo


def constructStringInfo(initialStr: str, pairData: "dict"):
  """Return a dictionary containing information about the string."""
  stringInfo = {}

  for key in pairData:
    stringInfo[key] = {
      "numCount": 0,
      "charToInsert": pairData[key],
    }

  # Loop through initial string
  for i in range(len(initialStr) - 1):
    if (initialStr[i:i + 2]) in stringInfo:
      stringInfo[initialStr[i:i + 2]]["numCount"] += 1

  return stringInfo

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open('inputFiles/day14.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputData: "list[str]" = [x for x in inputFromFile.split("\n") if x]
  pairData = {}
  for x in inputData[1:]:
    split = x.split(" -> ")

    pairData[split[0]] = split[1]

  initialStr = inputData[0]
  stringInfo = constructStringInfo(initialStr, pairData)
  for i in range(10):
    stringInfo = insertPairsEfficient(stringInfo)

  print(f"Difference between most common and least common (after 10): {getLetterCounts(stringInfo)}")

  stringInfo = constructStringInfo(initialStr, pairData)
  for i in range(40):
    stringInfo = insertPairsEfficient(stringInfo)

  print(f"Difference between most common and least common (after 40): {getLetterCounts(stringInfo)}")
  print("--- %s seconds ---" % (time.perf_counter() - startTime))