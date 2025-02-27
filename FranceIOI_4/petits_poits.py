import sys
import math

def main():
    sys.stdin = open("input.txt", "r")
    
    peas = int(sys.stdin.readline())
    
    factorials = (1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600)
    boxes = [0] * 12
    
    factorial = 1
    
    for i in range(1, 13):
        if peas < factorials[i - 1]:
            factorial = i - 1
            break
        elif i == 12:
            factorial = 12
        
    print(factorial)
    
    for i in range(factorial - 1, -1, -1):
        boxes[i] = peas // factorials[i]
        peas %= factorials[i]

    for i in range(factorial):
        print(boxes[i], end=" ")
    
    print()
    
if __name__ == "__main__":
    main()