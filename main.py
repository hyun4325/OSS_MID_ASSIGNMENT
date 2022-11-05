
from operator import ne
import os
import re
from calculation import add_function as add
from calculation import subtract_function as sub
from calculation import multiply_function as mul
from calculation import divide_function as div
from logfile import calculation_log as savelog
from logfile import error_log as saveerror

path = os.path.dirname(os.path.realpath(__file__))

cal_log = path + "\logfile\calculation_log.txt"
error_log = path +  "\logfile\error_log.txt"

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
            func = '+'
            result = add.add(num1, num2)
            print(result)
        elif choice == '2':
            func = '-'
            result = sub.sub(num1, num2)
            print(result)
        elif choice == '3':
            func = '*'
            result = mul.mul(num1, num2)
            print(result)
        elif choice == '4':
            func = '/'
            result = div.div(num1, num2)
            if(result == "Can not divide by 0") :
                saveerror.save_error(error_log, result , "Enter second number",'0')
            print(result)
            
        if(result != "Can not divide by 0") :
            savelog.save_log(cal_log, func, str(num1), str(num2), str(result))
        

        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ").lower()            
            if next_calculation == "no": 
                remind = input("Are you sure? (yes/no): ").lower()
                if remind == "yes":  
                    progress = False
                    break
                elif remind == "no":
                    progress = True
                    break
                else:
                    print("input error")
                    saveerror.save_error(error_log ,"input error", "Are you sure? (yes/no)",remind)
                    continue    
            elif next_calculation == "yes":
                progress = True
                break
            elif next_calculation == "why?":
                continue
            else:
                print("input error")
                saveerror.save_error(error_log ,"input error", "Let's do next calculation? (yes/no)",next_calculation)
                continue
        if progress == False:
            break
     


    else:
        print("Invalid Input")
        saveerror.save_error(error_log ,"Invalid Input", "Enter choice(1/2/3/4)",choice)

