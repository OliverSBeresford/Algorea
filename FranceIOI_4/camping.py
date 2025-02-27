import sys

"""

input:
6 7
1 0 0 1 0 0 1
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 1 0 0 0 0 1
1 0 0 0 1 0 1

output:
4

input:
5 7
0 0 0 1 1 1 1
0 0 0 1 1 1 1
0 0 0 1 1 1 1
1 1 1 1 1 0 0
1 1 1 1 1 0 0

output:
3

"""

def max_square_area(grid, rows, cols):
    if rows == 0 or cols == 0:
        return 0

    # DP table to store largest square ending at (i, j)
    area_map = [[0] * cols for _ in range(rows)]
    max_size = 0

    # Fill DP table
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                # First row or first column is always just 1 square by 1 square
                if row == 0 or col == 0:
                    area_map[row][col] = 1
                else:
                    # Checking maximum sizes of squares ending in the three squares around the current square
                    area_map[row][col] = min(area_map[row-1][col], area_map[row][col-1], area_map[row-1][col-1]) + 1
                
                # Track max square size
                max_size = max(max_size, area_map[row][col])

    return max_size

def main():
    sys.stdin = open("input.txt", "r")
    
    rows, cols = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
    
    max_area = max_square_area(grid, rows, cols)
    print(max_area)

if __name__ == "__main__":
    main()
