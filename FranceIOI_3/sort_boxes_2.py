import sys
import operator

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_boxes = int(input())
boxes = [list(map(int, input().split())) for _ in range(num_boxes)]

print("\n".join(str(i[0]) + " " + str(i[1]) for i in sorted(boxes, key=operator.itemgetter(1, 0))))