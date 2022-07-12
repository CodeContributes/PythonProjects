player1 = input("Welcome to Tic Tac Toe! Choose, X or O?")

if player1 == 'X':
   player2 = 'O'
else:
    player2 = 'X'

board = []
for row in range(3):
    board.append([""] * 3)


def isValid(row, col):
    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False

    return board[row][col] == ""


def playerMakeMove(mark):
    isValidMove = False

    while not isValidMove:
        inputRow = int(input('Pick a row'))
        inputColumn = int(input('Pick a column'))

        isValidMove = isValid(inputRow, inputColumn)
        if not isValidMove:
            print("Please enter a valid input.")

        board[inputRow][inputColumn] = mark


def checkHorizontal():
    for row in range(3):
        mark = board[row][0]
        if mark == "":
            continue

        matches = 1
        for col in range(1, 3):
            if mark == board[row][col]:
                matches += 1

        if matches == 3:
            return True
    return False


def checkVertical():
    for col in range(3):
        mark = board[0][col]
        if mark == "":
            continue

        matches = 1
        for row in range(1, 3):
            if mark == board[row][col]:
                matches += 1

        if matches == 3:
            return True
    return False


def diagonal(row, col, increment):
    mark = board[row][col]
    if mark == "":
        return False

    matches = 1
    for _ in range(2):
        row += increment
        col += increment
        if mark == board[row][col]:
            matches += 1

    return matches == 3


def checkDiagonal():
    return diagonal(0, 0, 1) or diagonal(0, 2, -1)


def checkWinner():
    return checkHorizontal() or checkVertical() or checkDiagonal()


'''for row in range(3):
    print(board[row])
print(checkWinner())'''
# This little piece of code right here, messed me up so bad.


def CheckBoardFilled():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True


def ticTacToe():
    while True:
        for mark in [player1, player2]:
            playerMakeMove(mark)

            for row in range(3):
                print(board[row])

            if checkWinner():
                print(mark + " wins!")
                return

            if CheckBoardFilled():
                print("Game Over.")
                return


ticTacToe()
