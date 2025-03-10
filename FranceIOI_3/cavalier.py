import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

board = [input() for _ in range(8)]

transforms = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

can_capture = False

for y, row in enumerate(board):
    for x, piece in enumerate(row):
        if piece != 'C':
            continue
        for transform in transforms:
            if -1 < y + transform[1] < 8 and -1 < x + transform[0] < 8 and board[y + transform[1]][x + transform[0]].islower():
                can_capture = True
                break

if can_capture:
    print('yes')
else:
    print('no')
    