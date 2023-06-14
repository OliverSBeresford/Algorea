nbnombres = int(input())
num = 0
num1 = int(input())
num2 = int(input())

for i in range(2, nbnombres):
    num3 = int(input())

    if num2 > num1 and num2 > num3:
        num += 1

    num1 = num2
    num2 = num3

print(num)