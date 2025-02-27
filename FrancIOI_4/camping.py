import numpy as np

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

# def area(grid, start_row, start_col):
#     rows, cols = len(grid), len(grid[0])
    
#     square_size = 1
    
#     while start_row >= 0 and start_row + square_size < rows and start_col >= 0 and start_col + square_size < cols:
#         for row in range(start_row, start_row + square_size + 1):
#             if grid[row][start_col + square_size] == 1:
#                 return square_size
            
#         for col in range(start_col, start_col + square_size + 1):
#             if grid[start_row + square_size][col] == 1:
#                 return square_size
                
#         square_size += 1
    
#     return square_size
def area(grid, start_row, start_col):
    rows, cols = np.shape(grid)
    
    square_size = 1
    
    while start_row >= 0 and start_row + square_size < rows and start_col >= 0 and start_col + square_size < cols:
        if np.any(grid[start_row:start_row + square_size + 1, start_col + square_size]):
            return square_size
            
        if np.any(grid[start_row + square_size, start_col:start_col + square_size]):
            return square_size
                
        square_size += 1
    
    return square_size

def main():
    rows, cols = map(int, input().split())
    grid = np.array([list(map(int, input().split())) for _ in range(rows)])
    max_area = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                max_area = max(max_area, area(grid, row, col))
                
    print(max_area)
    
if __name__ == "__main__":
    main()