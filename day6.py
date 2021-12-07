import time

def simulateFishCount(ages: "list[int]"):
  """Simulate one fish creation cycle."""

  newAges = []

  for i in range(len(ages)):
    if (ages[i] == 0):
      # Create new fish
      newAges.append(8)
      newAges.append(6)

    else:
      newAges.append(ages[i] - 1)
  
  return newAges

def simulateFishCountFast(ages: "list[int]", days: int):
  """Return the number of fish after a specified amount of days."""

  # Create list of fish counters
  fishTracker = [0] * 9
  # Index of list is the counter #
  # Value is the number of fish with that counter #

  # Initialize
  for age in ages:
    fishTracker[age] += 1

  # Move numbers in fish tracker around for number of days
  for _ in range(days):
    numFishAt0 = fishTracker[0]
    
    # Shift numbers up
    fishTracker[0] = 0
    for i in range(1, 9):
      fishTracker[i - 1] = fishTracker[i]
    fishTracker[8] = 0

    # Add values of counter 6 and 8 for # of fish at counter 0
    fishTracker[6] += numFishAt0
    fishTracker[8] += numFishAt0

  return sum(fishTracker)

# Read the input file
if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day6.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [x for x in inputFromFile.split('\n') if x]
  fishAges: "list[int]" = [int(x) for x in inputList[0].split(',') if x]

  print(f"Number of fish in 80 days: {simulateFishCountFast(fishAges, 80)}")
  print(f"Number of fish in 256 days: {simulateFishCountFast(fishAges, 256)}")

  print("--- %s seconds ---" % (time.time() - startTime))