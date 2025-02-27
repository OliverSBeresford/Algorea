nbcases = int(input())
num = 0
list = []
for i in range(0, nbcases):
    list.append(int(input()))
for i in range(0, 10):
    print(num+1)
    print()
    num = list[num] - 1