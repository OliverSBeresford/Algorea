import sys

def main():
    sys.stdin = open("input.txt", "r")
    
    num_jackets = int(sys.stdin.readline())
    jackets = []
    
    max_included = 0
    
    for i in range(num_jackets):
        jacket = list(map(int, input().split()))
        jackets.append(jacket)
    
    for jacket in jackets:
        included = 0
        for i in range(num_jackets):
            if jackets[i][0] >= jacket[0] and jackets[i][1] <= jacket[1]:
                included += 1
        if included - 1 >= max_included:
            max_included = included - 1
    
    print(max_included)
    
if __name__ == "__main__":
    main()