import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_boxes = int(input())
boxes = list(map(int, input().split()))

print(" ".join(str(i) for i in sorted(boxes)))