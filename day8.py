import time

def getMap(inputLine: str):
  """Get a list with the mapped signal wires."""

  p = [''] * 7
  g1 = [''] * 2
  g2 = [''] * 2

  signalPatterns = inputLine.split(" | ")[0].split(" ")

  missingLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];

  # Populate g1
  for digit in signalPatterns:
    if (len(digit) == 2):
      g1[0] = digit[0]
      g1[1] = digit[1]

      missingLetters.remove(digit[0])
      missingLetters.remove(digit[1])
      break

  # Populate g2 and p0
  for digit in signalPatterns:
    if (len(digit) == 3):
      # Populate p0 with letter not in g1
      for i in range(3):
        if (digit[i] not in g1):
          p[0] = digit[i]
          missingLetters.remove(digit[i])
          break
    elif (len(digit) == 4):
      # Find letters not in g1
      for i in range(4):
        if (digit[i] not in g1):
          g2[g2.index('')] = digit[i]
          missingLetters.remove(digit[i])

  # Digits with length of 5
  # There will always be 3 of these
  withLen5 = [digit for digit in signalPatterns if len(digit) == 5]

  confirmedTwo = None

  for i in missingLetters:
    # Find unique letter
    filtered = [digit for digit in withLen5 if digit.find(i) > -1]
    if (len(filtered) == 1):
      confirmedTwo = filtered[0]
      p[4] = i
      p[6] = missingLetters[missingLetters.index(i) - 1]
  
  threeOrFive = [digit for digit in withLen5 if digit != confirmedTwo]

  confirmedFive = None
  confirmedThree = None

  for digit in threeOrFive:
    lettersInG1 = []

    for letter in digit:
      if (letter in g1):
        lettersInG1.append(letter)

    if (len(lettersInG1) == 2):
      confirmedThree = digit

  confirmedFive = threeOrFive[threeOrFive.index(confirmedThree) - 1]

  for letter in confirmedThree:
    if (letter not in confirmedFive):
      p[2] = letter

  for letter in confirmedFive:
    if (letter not in confirmedThree):
      p[1] = letter
  
  for letter in confirmedThree:
    if (letter not in confirmedTwo):
      p[5] = letter

  for letter in g2:
    if (letter not in p):
      p[3] = letter
      break

  return p

def getFilledPositions(digit: str, posMap: "list[str]"):
  """Get the filled positions of the digit."""

  result = []
  
  for i in digit:
    result.append(posMap.index(i))

  result.sort()
  return result


def getSumOfOutputValues(inputList: "list[str]"):
  """Get the sum of all the output values."""
  
  digitProcessor = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
  ]

  result = 0

  for line in inputList:
    digits = line.split(" | ")[1].split(" ")
    posMap = getMap(line)

    decoded = ""

    for digit in digits:
      filledPositions = getFilledPositions(digit, posMap)
      decoded += str(digitProcessor.index(filledPositions))

    result += int(decoded)

  return result


def countEasyDigits(inputList: "list[str]"):
  """Count the number of digits that have unique segment lengths."""

  count = 0

  uniqueSegmentLengths = (2, 4, 3, 7)

  for line in inputList:
    digits = line.split(" | ")[1].split(" ")

    for digit in digits:
      if (len(digit) in uniqueSegmentLengths):
        count += 1

  return count

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day8.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split('\n') if x]

  countOfEasyDigits = countEasyDigits(inputList)
  print(f"Times where 1, 4, 7, and 8 appear: {countOfEasyDigits}")

  resultSum = getSumOfOutputValues(inputList)
  print(f"Sum of all output values: {resultSum}")

  print("--- %s seconds ---" % (time.time() - startTime))