import sys
def main():
    nbjours = int(input())
    dicc = {}
    start = 0
    nbpourchaque = [0 for x in range(nbjours)]
    couches = [0 for x in range(200000)]
    for i in range(nbjours):
        new = int(input())
        for x in range(new):
            couches[start + new] = i
            nbpourchaque[i] += 1
        start += 1
    
    [sys.stdout.write(str(x)) for x in nbpourchaque]
            
main()