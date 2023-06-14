def main():
    nbnombres = int(input())   # Read the number of input values
    num = 0                   # Initialize the total to 0
    num1 = int(input())       # Read the first input value

    for i in range(nbnombres - 1):
        num2 = int(input())   # Read the next input value

        # Compare the previous value (num1) with the current value (num2)
        if num1 < num2:
            num += (num2 - num1) * 2   # If num2 is greater, add the difference multiplied by 2 to the total
        elif num1 > num2:
            num += num1 - num2         # If num1 is greater, add the difference to the total

        num1 = num2   # Set the current value as the new previous value for the next iteration

    print(num)   # Print the calculated total

main()