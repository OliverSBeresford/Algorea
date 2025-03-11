import sys

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        if lst[left] >= target:
            return left
        if lst[right] < target:
            return right + 1
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

boxes_initial, boxes_added = map(int, input().split())
boxes = list(map(int, input().split()))
new_boxes = list(map(int, input().split()))

for i in range(boxes_added):
    index = binary_search(boxes, new_boxes[i])
    print(index, end=" ")
    boxes.insert(index, new_boxes[i])

print()
print(*boxes)