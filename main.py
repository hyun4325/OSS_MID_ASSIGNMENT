from calculation import add_function as add

print("Select operation.")
print("1.Add")

while True:
    # take input from the user
    choice = input("Enter choice(1): ")

    # check if choice is one of the four options
    if choice in ('1'):

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = int(add.add(num1, num2))
            print(result)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")