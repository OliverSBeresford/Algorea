nbnombres = int(input())
num = 0
num1 = int(input())
for i in range(nbnombres - 1):
    num2 = int(input())
    if num1 < num2:
        num += (num2 - num1) * 2
    elif num1 > num2:
        num += num1 - num2
    num1 = num2
print(num)