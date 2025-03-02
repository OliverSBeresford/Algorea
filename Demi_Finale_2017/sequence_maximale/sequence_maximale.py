import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

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
    
    if window - 1 >= 0 and lengths[window - 1] > max_length:
        max_length = lengths[window - 1]
    
    if current > max_length and current < length:
        max_length = current
        
    while current >= 2 and lengths[window] != 2:
        window -= 1
    
    right_length = current - lengths[window] + 1
    left_length = lengths[window - 2]
    
    if window - 2 >= 0 and numbers[window - 2] < numbers[window] and left_length + right_length > max_length:
        max_length = left_length + right_length
        
    while lengths[window] != 1:
        window -= 1
        
    right_length = current - lengths[window] + 1
    left_length = lengths[window - 2]
    
    if window - 2 >= 0 and numbers[window - 2] < numbers[window] and left_length + right_length > max_length:
        max_length = left_length + right_length
    
    window -= 1

print(max_length)
