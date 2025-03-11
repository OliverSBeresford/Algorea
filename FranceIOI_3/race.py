import sys

sys.stdin = open("input.txt", "r") # Comment this line out when submitting on the platform

num_cars = int(input())
cars = list(map(int, input().split()))
car_positions = {cars[i]: i for i in range(num_cars)}
moves = []
print(car_positions)

for i in range(1, num_cars + 1):
    for j in range(car_positions[i], i - 1, -1):
        moves.append((cars[j - 1], i))
        cars[j], cars[j - 1] = cars[j - 1], cars[j]
        car_positions[cars[j]] = j
        car_positions[cars[j - 1]] = j - 1

print(len(moves))
for move in moves:
    print(*move)
