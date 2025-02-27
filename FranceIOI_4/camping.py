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
def area(grid, rows, cols, start_row, start_col, max_area):
    square_size = 1
    
    if start_row < 0 or start_row + max_area >= rows or start_col < 0 or start_col + max_area >= cols:
        return 0
    
    while start_row + square_size < rows and start_col + square_size < cols:
        if any([row[start_col + square_size] for row in grid[start_row:start_row + square_size + 1]]):
            return square_size
            
        if any([col for col in grid[start_row + square_size][start_col:start_col + square_size]]):
            return square_size
                
        square_size += 1
    
    return square_size

def potential_area(grid, rows, cols, start_row, start_col):
    max_length = 1
    
    for col in range(start_col, cols):
        if grid[start_row][col] == 1:
            max_length = col - start_col
            break
        elif col == cols - 1:
            max_length = cols - start_col + 1
            break
    for row in range(start_row, rows):
        if grid[row][start_col] == 1:
            max_length = min(max_length, row - start_row)
            break
        elif row == rows - 1:
            max_length = rows - start_row + 1
            break
    
    return max_length

def main():
    sys.stdin = open("input.txt", "r")
    
    rows, cols = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
    max_area = 0
    max_potential = 0
    areas = dict()
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                # Getting the potential area for this 0
                potential = potential_area(grid, rows, cols, row, col)
                # Resetting the max potential to iterate at the end starting from max to 0
                max_potential = max(max_potential, potential)
                # Adding the potential area to the dictionary
                if potential not in areas:
                    areas[potential] = []
                areas[potential].append((row, col))
                
    for potential in range(max_potential, 0, -1):
        if potential not in areas:
            continue
    
        if max_area >= potential:
            break
        
        for row, col in areas[potential]:
            max_area = max(max_area, area(grid, rows, cols, row, col, max_area))
            if max_area == potential:
                break
                
    print(max_area)
    
if __name__ == "__main__":
    main()