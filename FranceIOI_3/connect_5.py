import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]

# Extract rows, columns, and diagonals from the board
rows = board
columns = [[board[j][i] for j in range(size)] for i in range(size)]
diagonals = [[board[i + j][j] for j in range(size - i)] for i in range(size)]
diagonals += [[board[j][i + j] for j in range(size - i)] for i in range(1, size)]
diagonals += [[board[i - j][j] for j in range(i + 1)] for i in range(size - 1)]
diagonals += [[board[size - 1 - j][i + j] for j in range(size - i)] for i in range(size)]

def check_five_consecutive(lst, player):
    return any(lst[i:i+5] == [player]*5 for i in range(len(lst) - 4))

def check_winner(lines):
    for line in lines:
        if check_five_consecutive(line, 1):
            return 1
        if check_five_consecutive(line, 2):
            return 2
    return None

winner = check_winner(rows) or check_winner(columns) or check_winner(diagonals)

if winner:
    print(winner)
else:
    print(0)