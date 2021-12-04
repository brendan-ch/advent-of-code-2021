import time
import copy

class BoardNumber:
  """Represents a number on a board."""
  def __init__(self, number: int):
    self.num = number
    self.filled = False

class Board:
  """Represents a single 5x5 board with board numbers."""
  def __init__(self, board2DList: "list[list[BoardNumber]]") -> None:
    self.board2DList = board2DList

  def getCoord(self, x: int, y: int):
    return self.board2DList[y][x]

  def fillCoord(self, x: int, y: int):
    self.getCoord(x, y).filled = True

  def getSumOfUnfilledNums(self):
    """Return the sum of all unfilled numbers."""
    calculatedSum = 0

    for row in self.board2DList:
      for num in row:
        if (not num.filled):
          calculatedSum += num.num

    return calculatedSum

  def fillCoordByNum(self, num: int):
    """Search through the 2D list and fill the correct number (if existent)"""

    for row in self.board2DList:
      for existingNum in row:
        if (existingNum.num == num):
          existingNum.filled = True
          self.lastFilled = num
          return;

  def checkWinner(self) -> bool:
    """Return true if there is a board winner."""
    # Check columns
    for x in range(0, 5):
      if (self.getCoord(x, 0).filled
        and self.getCoord(x, 1).filled
        and self.getCoord(x, 2).filled
        and self.getCoord(x, 3).filled
        and self.getCoord(x, 4).filled
      ):
        return True
    
    # Check rows
    for y in range(0, 5):
      if (self.getCoord(0, y).filled
        and self.getCoord(1, y).filled
        and self.getCoord(2, y).filled
        and self.getCoord(3, y).filled
        and self.getCoord(4, y).filled
      ):
        return True

    # Otherwise return false
    return False

def createBoards(inputList: "list[str]"):
  """Create a list of boards given the input list."""

  # List of boards that will be returned
  boardList = []

  # The temporary board being created
  board2DList = []

  for line in inputList:
    # Create an list of BoardNumber's and append to list
    # If length of board2DList is 5, clear the list

    numList = [BoardNumber(int(num)) for num in line.split(' ') if len(num) > 0]
    board2DList.append(numList)

    if (len(board2DList) >= 5):
      # Clear board
      boardList.append(Board(board2DList))
      board2DList = []

  return boardList

def simulateGames(boardList: "list[Board]", order: "list[int]") -> "Board":
  """Simulate games until one board has a winner."""

  copiedOrder = order.copy()
  copiedBoardList = copy.deepcopy(boardList)
  winningBoard = None

  while (winningBoard == None):
    # Loop through all boards and simulate a game
    for board in copiedBoardList:
      board.fillCoordByNum(copiedOrder[0])
      
      if (board.checkWinner()):
        winningBoard = board
        break

    copiedOrder.pop(0)

  return winningBoard

def simulateUntilLastGame(boardList: "list[Board]", order: "list[int]") -> "Board":
  """Simulate games and return the last board to win."""

  copiedBoardList = copy.deepcopy(boardList)
  copiedOrder = order.copy()
  lastBoardWon = None

  while (len(copiedBoardList) > 0):
    for board in copiedBoardList.copy():
      board.fillCoordByNum(copiedOrder[0])

      if (board.checkWinner()):
        lastBoardWon = board
        copiedBoardList.remove(board)

    copiedOrder.pop(0)

  return lastBoardWon

# Read the input file
if __name__ == "__main__":
  startTime = time.time()

  with open('inputFiles/day4.txt', 'r') as inputFile:
    inputFromFile = inputFile.read()

  # Get input list
  inputList = [x for x in inputFromFile.split('\n') if x]

  # First line are the order to draw numbers
  order = [int(x) for x in inputList[0].split(',')]

  # Store list of 2D lists of board numbers
  boardList = createBoards(inputList[1:])
  winningBoard = simulateGames(boardList, order)

  print(f"Score of first winning board: {winningBoard.getSumOfUnfilledNums() * winningBoard.lastFilled}")

  lastWinningBoard = simulateUntilLastGame(boardList, order)
  print(f"Score of last winning board: {lastWinningBoard.getSumOfUnfilledNums() * lastWinningBoard.lastFilled}")

  print("--- %s seconds ---" % (time.time() - startTime))