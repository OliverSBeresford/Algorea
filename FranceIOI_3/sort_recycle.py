import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_boxes = int(input())
recycles = [input() for _ in range(num_boxes)]

print("\n".join(sorted(recycles)))