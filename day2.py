import time

def calculatePositionDepthAim(input: 'list[str]'):
  h = 0
  d = 0
  a = 0

  for line in input:
    value = int(line[-1:])

    if (line.startswith('forward')):
      h += value
      d += (a * value)
    elif (line.startswith('down')):
      a += value
    elif (line.startswith('up')):
      a -= value

  return h * d

def calculatePositionDepth(input: 'list[str]'):
  h = 0
  d = 0

  for line in input:
    value = int(line[-1:])

    if (line.startswith('forward')):
      h += value
    elif (line.startswith('down')):
      d += value
    elif (line.startswith('up')):
      d -= value

  return h * d

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day2.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [x for x in inputFromFile.split('\n') if x]

  positionDepthMultiplied = calculatePositionDepth(inputList)
  print(f"Position and depth multiplied: {positionDepthMultiplied}")
  
  positionDepthMultipliedAim = calculatePositionDepthAim(inputList)
  print(f"Position and depth multiplied (with aim): {positionDepthMultipliedAim}")
  
  print("--- %s seconds ---" % (time.time() - startTime))