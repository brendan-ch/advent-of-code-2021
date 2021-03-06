import time

def convertToBin(hexValue: str):
  """Convert the hexadecimal string to binary, using a hex-to-binary table."""

  hexToBin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
  }

  binValue = ''
  for letter in hexValue:
    binValue += hexToBin[letter]

  return binValue

def evaluateValues(binary: str):
  """Decode the given packet and return the evaluation of the values."""
  if (len(binary) <= 7):
    # Invalid packet
    return (0, len(binary))

  # Check packet type ID
  ptId = int(binary[3:6], 2)
  endIndex = 0
  value = 0

  # Values of each individual subpacket
  tempValues = []

  if (ptId == 4):
    tempStr = '';
    tempBin = '';
    parseStart = 6
    # Parse groups until end group reached
    while (tempStr != '0'):
      tempStr = binary[parseStart]
      tempBin += binary[parseStart + 1:parseStart + 5]
      parseStart += 5

    value = int(tempBin, 2)
    endIndex = parseStart
    return (value, endIndex)

  # Switch between ptId values
  ltId = binary[6]
  if (ltId == '0'):
    # Check next 15 bits for packet length
    packetLength = int(binary[7:22], 2)
    nextStr = binary[22:22 + packetLength]
    endIndex = 22

    while (len(nextStr) > 0):
      result = evaluateValues(nextStr)
      tempValues.append(result[0])
      endIndex += len(nextStr) - len(nextStr[result[1]:])
      nextStr = nextStr[result[1]:]

  elif (ltId == '1'):
    # Check next 11 bits for # of subpackets
    numPackets = int(binary[7:18], 2)
    tempStartIndex = 0
    endIndex = 18

    for _ in range(numPackets):
      result = evaluateValues(binary[18 + tempStartIndex:])
      tempValues.append(result[0])
      tempStartIndex += result[1]

    endIndex += tempStartIndex

  # Do something with tempValues based on the ptId
  if (ptId == 0):
    value = sum(tempValues)
  elif (ptId == 1):
    value = 1
    for i in tempValues:
      value *= i
  elif (ptId == 2):
    value = min(tempValues)
  elif (ptId == 3):
    value = max(tempValues)
  elif (ptId == 5):
    value = 1 if tempValues[0] > tempValues[1] else 0
  elif (ptId == 6):
    value = 1 if tempValues[0] < tempValues[1] else 0
  elif (ptId == 7):
    value = 1 if tempValues[0] == tempValues[1] else 0

  return (value, endIndex)

def sumVersionNumbers(binary: str):
  """Decode the given packet and return the version number sum."""
  if (len(binary) <= 7):
    # Invalid packet
    return (0, len(binary))

  # Check version number and packet type ID
  version = int(binary[:3], 2)
  literalValue = binary[3:6] == '100'
  endIndex = 0

  if (literalValue):
    tempStr = '';
    parseStart = 6
    # Parse groups until end group reached
    while (tempStr != '0'):
      tempStr = binary[parseStart]
      parseStart += 5

    endIndex = parseStart

  else:
    ltId = binary[6]
    if (ltId == '0'):
      # Check next 15 bits for packet length
      packetLength = int(binary[7:22], 2)
      nextStr = binary[22:22 + packetLength]
      endIndex = 22

      while (len(nextStr) > 0):
        result = sumVersionNumbers(nextStr)
        version += result[0]
        endIndex += len(nextStr) - len(nextStr[result[1]:])
        nextStr = nextStr[result[1]:]

    elif (ltId == '1'):
      # Check next 11 bits for # of subpackets
      numPackets = int(binary[7:18], 2)
      tempStartIndex = 0
      endIndex = 18

      for _ in range(numPackets):
        result = sumVersionNumbers(binary[18 + tempStartIndex:])
        version += result[0]
        tempStartIndex += result[1]

      endIndex += tempStartIndex

  return (version, endIndex)

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open("inputFiles/day16.txt", "r") as inputFile:
    inputFromFile = inputFile.read()

  binary = convertToBin(inputFromFile)

  print(f'Sum of version numbers: {sumVersionNumbers(binary)[0]}')
  print(f'Evaluation of values: {evaluateValues(binary)[0]}')

  print("--- %s seconds ---" % (time.perf_counter() - startTime))