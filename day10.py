import time

def getSyntaxScore(line: str):
  """Get the syntax error score for a line. Returns 0 if line is incomplete."""

  # Track openers as of position in loop
  openerTracker = []

  # openers = ('[', '(', '{', '<')
  pairings = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>',
  }

  syntaxErrorScores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }

  for char in line:
    if (char in list(pairings.keys())):
      openerTracker.append(char)

    # Correct closing for chunk
    elif (char == pairings[openerTracker[-1]]):
      openerTracker.pop()

    else:
      # Syntax error
      return syntaxErrorScores[char]

  return 0

def getAutocompleteScore(line: str):
  """Get the autocomplete score for a line."""

  # Track openers as of position in loop
  openerTracker = []

  # openers = ('[', '(', '{', '<')
  pairings = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>',
  }

  scoringTable = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
  }

  for char in line:
    if (char in list(pairings.keys())):
      openerTracker.append(char)

    # Correct closing for chunk
    elif (char == pairings[openerTracker[-1]]):
      openerTracker.pop()

  openerTracker.reverse()
  completionString = [pairings[i] for i in openerTracker]
  completionScore = 0
  
  for i in completionString:
    completionScore *= 5
    completionScore += scoringTable[i]

  return completionScore

if (__name__ == "__main__"):
  startTime = time.time()

  with open('inputFiles/day10.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  inputList = [x for x in inputFromFile.split('\n') if x]

  syntaxErrorScore = 0
  for line in inputList.copy():
    score = getSyntaxScore(line)
    if (score > 0):
      syntaxErrorScore += score
      inputList.remove(line)

  print(f"Syntax error score: {syntaxErrorScore}")

  # Input list should now only have incomplete lines
  autocompleteScores = []
  for line in inputList:
    autocompleteScores.append(getAutocompleteScore(line))

  autocompleteScores.sort()
  print(f"Middle autocomplete score: {autocompleteScores[int(len(autocompleteScores) / 2 - 0.5)]}")

  print("--- %s seconds ---" % (time.time() - startTime))