import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_plastics = int(input())
plastics = set(map(int, input().split()))
num_queries = int(input())
queries = [int(input()) for _ in range(num_queries)]

for i in queries:
    if i in plastics:
        print(1)
    else:
        print(0)