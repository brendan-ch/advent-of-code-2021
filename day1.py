import time

def getMeasurementWindowSums(measurements: "list[int]"):
  sums = []

  for i in range(len(measurements) - 2):
    sums.append(measurements[i] + measurements[i + 1] + measurements[i + 2])

  return sums

def countMeasurements(measurements: "list[int]"):
  count = 0

  for i in range(1, len(measurements)):
    if (measurements[i] > measurements[i - 1]):
      count += 1

  return count

if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day1.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [int(x) for x in inputFromFile.split('\n') if x]

  count = countMeasurements(inputList)
  print(f'Number increased: {count}')

  sums = getMeasurementWindowSums(inputList)
  countSums = countMeasurements(sums)
  print(f'Sums increased: {countSums}')
  
  print("--- %s seconds ---" % (time.time() - startTime))