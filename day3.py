import time

def getLeastCommonBit(input: "list[str]", index: int):
  """Return the least common bit at index."""

  bit0 = 0
  bit1 = 0

  for numStr in input:
    if (numStr[index:index + 1] == "0"):
      bit0 += 1
    elif (numStr[index:index + 1] == "1"):
      bit1 += 1

  if (bit0 <= bit1):
    return 0
  else:
    return 1

def getMostCommonBit(input: "list[str]", index: int):
  """Return the most common bit at index."""

  bit0 = 0
  bit1 = 0

  for numStr in input:
    if (numStr[index:index + 1] == "0"):
      bit0 += 1
    elif (numStr[index:index + 1] == "1"):
      bit1 += 1

  if (bit0 > bit1):
    return 0
  else:
    return 1

def getGammaRateBit(input: "list[str]"):
  """Parse the input list and return the gamma rate in bits."""

  result = [str(getMostCommonBit(input, index)) for index in range(0, len(input[0]))]
  resultStr = "".join(result)

  return int(resultStr)

def getEpsilonRateBit(input: "list[str]"):
  """Parse the input list and return the epsilon rate in bits."""

  result = [str(getLeastCommonBit(input, index)) for index in range(0, len(input[0]))]
  resultStr = "".join(result)

  return int(resultStr)

def filterOxygenGeneratorRating(input: "list[str]", index: int):
  """Take an input list and return a filtered list, based on the bit at the index."""

  mostCommon = str(getMostCommonBit(input, index))
  newList = [inputData for inputData in input if (inputData[index:index + 1] == mostCommon)]

  return newList

def filterCO2ScrubberRating(input: "list[str]", index: int):
  """Take an input list and return a filtered list, based on the bit at the index."""

  leastCommon = str(getLeastCommonBit(input, index))
  newList = [inputData for inputData in input if (inputData[index:index + 1] == leastCommon)]

  return newList

def getOxygenGeneratorRating(input: "list[str]"):
  """Filter out the oxygen generator rating."""

  newList = input
  index = 0
  while (len(newList) > 1):
    newList = filterOxygenGeneratorRating(newList, index)
    index += 1

  return newList[0]

def getCO2ScrubberRating(input: "list[str]"):
  """Filter out the CO2 scrubber rating."""

  newList = input
  index = 0
  while(len(newList) > 1):
    newList = filterCO2ScrubberRating(newList, index)
    index += 1

  return newList[0]


# Read the input file
if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day3.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [x for x in inputFromFile.split('\n') if x]

  # Convert to integer
  gammaRate = int(str(getGammaRateBit(inputList)), 2)
  epsilonRate = int(str(getEpsilonRateBit(inputList)), 2)

  print(f'Power consumption rate: {gammaRate * epsilonRate}')

  oxygenGeneratorRating = int(getOxygenGeneratorRating(inputList), 2)
  co2ScrubberRating = int(getCO2ScrubberRating(inputList), 2)

  print(f'Life support rating: {oxygenGeneratorRating * co2ScrubberRating}')

  print("--- %s seconds ---" % (time.time() - startTime))