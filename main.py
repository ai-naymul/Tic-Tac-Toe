xState = [0,0,0,0,0,0,0,0,0]
oState = [0,0,0,0,0,0,0,0,0]
TURN = 1
def printboard(xState, oState):
  one = 'X' if xState[0] else ('O' if oState[0] else 0)
  two = 'X' if xState[1] else ('O' if oState[1] else 1)
  three = 'X' if xState[2] else ('O' if oState[2] else 2)
  four = 'X' if xState[3] else ('O' if oState[3] else 3)
  five = 'X' if xState[4] else ('O' if oState[4] else 4)
  six = 'X' if xState[5] else ('O' if oState[5] else 5)
  seven = 'X' if xState[6] else ('O' if oState[6] else 6)
  eight = 'X' if xState[7] else ('O' if oState[7] else 7)
  nine = 'X' if xState[8] else ('O' if oState[8] else 8)
  ## Print the board
  print(f"{one} | {two} | {three}")
  print(f"----------")
  print(f"{four} | {five} | {six}")
  print(f"----------")
  print(f"{seven} | {eight} | {nine}")

def checkwin(xState,oState):
  wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for win in wins:
    if all(xState[i] == 1 for i in win):
      return "X"
    elif all(oState[i] == 1 for i in win):
      return "O"
  return None




print("Welcome to tic tac toe game")
while True:
  printboard(xState, oState)
  if TURN == 1:
    print("X's Choice")
    x_input = int(input("Please enter you choice between 0 to 8: "))
    xState[x_input] = 1
  else:
    print("O's Chance")
    o_input = int(input("Please enter you choice between 0 to 8: "))
    oState[o_input] = 1
  TURN = 1 - TURN
  winner = checkwin(xState,oState)
  if winner:
    printboard(xState,oState)
    print(f'Player {winner} won the match')
    break
