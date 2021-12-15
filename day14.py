import time
import copy

def getLetterCounts(initialStr: str):
  uniqueLetters = set(initialStr)
  
  letterCounts = [initialStr.count(letter) for letter in uniqueLetters]

  return max(letterCounts) - min(letterCounts)

def insertPairs(initialStr: str, pairData: "dict"):
  """Return a new string with the given pair data (inefficient)"""
  
  newStr = initialStr

  i = 0
  while i < len(newStr):
    if (newStr[i:i + 2]) in pairData:
      newStr = newStr[:i + 1] + pairData[newStr[i:i + 2]] + newStr[i + 1:]

      i += 1

    i += 1

  return newStr

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

  # string.count method is unreliable for this purpose
  # Loop through string manually

  for i in range(len(initialStr) - 1):
    if (initialStr[i:i + 2]) in stringInfo:
      stringInfo[initialStr[i:i + 2]]["numCount"] += 1

  return stringInfo

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open('inputFiles/day14.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputData: "list[str]" = [x for x in inputFromFile.split("\n") if x]

  initialStr = inputData[0]

  pairData = {}

  for x in inputData[1:]:
    split = x.split(" -> ")

    pairData[split[0]] = split[1]
    
  for i in range(10):
    initialStr = insertPairs(initialStr, pairData)

  print(f"Difference between most common and least common (after 10): {getLetterCounts(initialStr)}")

  initialStr = inputData[0]
  stringInfo = constructStringInfo(initialStr, pairData)

  for i in range(40):
    stringInfo = insertPairsEfficient(stringInfo)

  # Get unique letters
  allLetters = ""
  for key in pairData:
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

  print(f"Difference between most common and least common (after 40): {max(letterCounter.values()) - min(letterCounter.values())}")

  print("--- %s seconds ---" % (time.perf_counter() - startTime))