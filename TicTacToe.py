def User1Turn(board):
  pos = input("Enter X's position:")
  pos = int(pos)
  if(board[pos-1] != 0):
    print("Wrong Move...!!!")
    exit(0)
  board[pos-1] = 1

def User2Turn(board):
  pos = input("Enter O's position:")
  pos = int(pos)
  if(board[pos-1] != 0):
    print("Wrong Move...!!!")
    exit(0)
  board[pos-1] = -1

def ConstBoard(board):
  print("Current State of the Board: \n\n")
  for i in range (0, 9):
    if((i>0) and (i%3 == 0)):
      print("\n")
    if(board[i] == 0):
      print("_ ", end = " ")
    if(board[i] == 1):
      print("X ", end = " ")
    if(board[i] == -1):
      print("O ", end = " ")
  print("\n\n")


def analyzeboard(board):
  #who won
  cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  for i in range (0, 8):
    if((board[cb[i][0]] != 0) and (board[cb[i][0]] == board[cb[i][1]]) and (board[cb[i][1]]  == board[cb[i][2]])):
      return board[cb[i][0]]

  return 0

def CompTurn(board):
  pos = -1
  value = -2
  for i in range(0, 9):
    if(board[i] == 0):
      board[i] = 1
      score = 10
      board[i] = 0
      if(score > value):
        value = score
        pos = i
  board[pos] = i

def main():
  choice = int(input("Enter 1 for Single Player or 2 for Multi-Player"))
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

  if(choice == 1):
    #code to play against AI

    print("Computer : X Vs. You : O")
    player = input("Enter to play as 1st or 2nd")
    player = int(player)
    for i in range(0, 9):
      if(analyzeboard(board) != 0):
        break
      if((i+player)%2 == 0):
        CompTurn(board)
      else:
        ConstBoard(board)
        User1Turn(board)


  else:
    #code for multi-player
    for i in range (0, 9):
      if(analyzeboard(board) != 0):
        break
      if(i%2 == 0):
        ConstBoard(board)
        User1Turn(board)
      else:
        ConstBoard(board)
        User2Turn(board)


  x = analyzeboard(board)

  if(x == 0):
    ConstBoard(board)
    print("Draw!!!")

  elif(x == -1):
    ConstBoard(board)
    print("Player O has won!")

  elif(x == 1):
    ConstBoard(board)
    print("Player x has won!")
