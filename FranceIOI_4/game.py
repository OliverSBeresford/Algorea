import sys

def block(square, squares):
    if squares[square - 1] == 1:
        return []
    elif square == 1:
        squares[square - 1] = 1
        return [1]
    
    moves = []
    moves += block(square - 1, squares)
    
    for i in range(square - 2, 0, -1):
        moves += unblock(i, squares)

    moves.append(square)
    
    squares[square - 1] = 1
    
    return moves

def unblock(square, squares):
    if squares[square - 1] == 0:
        return []
    elif square == 1:
        squares[square - 1] = 0
        return [1]
    
    moves = []
    
    moves += block(square - 1, squares)
    
    for i in range(square - 2, 0, -1):
        moves += unblock(i, squares)
    
    moves.append(square)
    
    squares[square - 1] = 0
    
    return moves
        
def main():
    sys.stdin = open("input.txt", "r")
    
    num_squares = int(sys.stdin.readline())
    
    squares = [1] * num_squares
    
    moves = []
    
    for i in range(num_squares, 0, -1):
        moves += unblock(i, squares)
        
    for i in moves:
        print(i)

if __name__ == "__main__":
    main()