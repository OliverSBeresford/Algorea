def main():
    nbcases = int(input())
    num = 0
    list = [int(input()) for x in  range(nbcases)]
    for i in range(0, 10):
        print(num+1)
        print()
        num = list[num] - 1

main()