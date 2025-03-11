import sys

def closest_binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_plastics = int(input())
plastics = sorted(list(map(int, input().split())))
num_queries = int(input())
queries = [int(input()) for _ in range(num_queries)]

for i in queries:
    closest = closest_binary_search(plastics, i)
    if plastics[closest] == i:
        print(i)
        continue
    if abs(i - plastics[closest - 1]) <= abs(plastics[closest] - i):
        print(plastics[closest - 1])
    else:
        print(plastics[closest])