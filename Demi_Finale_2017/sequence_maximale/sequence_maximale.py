import sys

def main():
    sys.stdin = open("input.txt", "r")
    
    length = int(input())
    
    numbers = [int(input()) for _ in range(length)]
    lengths = [0] * length
    
    max_length = 1
    window = length - 1
    current = 0
    
    for i in range(length):
        if i == 0:
            lengths[i] = 1
        elif numbers[i] > numbers[i-1]:
            lengths[i] = lengths[i-1] + 1
        else:
            lengths[i] = 1
    
    while window >= 0:
        current = lengths[window]
        
        if current > max_length:
            max_length = current
        
        while lengths[window] != 1:
            window -= 1
        
        if window - 2 >= 0 and numbers[window - 2] < numbers[window] and lengths[window - 2] + current > max_length:
            max_length = current + lengths[window - 2]
        
        window -= 1
    
    print(max_length)
            
main()