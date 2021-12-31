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

def sumVersionNumbers(binary: str, startIndex: int):
  """Decode the given packet and return the version number sum."""
  if (len(binary) <= 7):
    # Invalid packet
    return (0, len(binary))

  # Check version number and packet type ID
  version = int(binary[startIndex:3 + startIndex], 2)
  literalValue = binary[3 + startIndex:6 + startIndex] == '100'
  endIndex = startIndex

  if (literalValue):
    tempStr = '';
    parseStart = 6 + startIndex
    # Parse groups until end group reached
    while (tempStr != '0'):
      tempStr = binary[parseStart]
      parseStart += 5

    endIndex = parseStart

  else:
    ltId = binary[6 + startIndex]
    if (ltId == '0'):
      # Check next 15 bits for packet length
      packetLength = int(binary[7 + startIndex:22 + startIndex], 2)
      nextStr = binary[22 + startIndex:22 + startIndex + packetLength]
      endIndex = 22

      while (len(nextStr) > 0):
        result = sumVersionNumbers(nextStr, 0)
        version += result[0]
        endIndex += len(nextStr) - len(nextStr[result[1]:])
        nextStr = nextStr[result[1]:]

    elif (ltId == '1'):
      # Check next 11 bits for # of subpackets
      numPackets = int(binary[7 + startIndex:18 + startIndex], 2)
      tempStartIndex = 0
      endIndex = 18

      for i in range(numPackets):
        result = sumVersionNumbers(binary[18 + startIndex + tempStartIndex:], 0)
        version += result[0]
        tempStartIndex += result[1]

      endIndex += tempStartIndex

  return (version, endIndex)

if (__name__ == "__main__"):
  startTime = time.perf_counter()

  with open("inputFiles/day16.txt", "r") as inputFile:
    inputFromFile = inputFile.read()

  binary = convertToBin(inputFromFile)

  print(f'Sum of version numbers: {sumVersionNumbers(binary, 0)[0]}')

  print("--- %s seconds ---" % (time.perf_counter() - startTime))