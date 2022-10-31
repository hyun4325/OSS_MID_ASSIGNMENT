from calculation import add_function as add
from calculation import subtract_function as sub
from calculation import multiply_function as mul
from calculation import divide_function as div

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options3
    if choice in ('1', '2', '3', '4'):

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = int(add.add(num1, num2))
            print(result)
        elif choice == '2':
            result = int(sub.sub(num1, num2))
            print(result)
        elif choice == '3':
            result = int(mul.mul(num1, num2))
            print(result)
        elif choice == '4':
            result = round(float(div.div(num1, num2)),2)
            print(result)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")