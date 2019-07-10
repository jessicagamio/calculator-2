from arithmetic import *

while True:


    # quit when user types q
    user_input=input(">")

    if user_input == 'q':
        break

    # else:
    else:

        # take the string and  tokenize by the space
        user_input_list = user_input.split(" ")
        


        #token 1 will be assigned float num1
        #token 2 will be assigned float num2

        num1 = float(user_input_list[1])
        num2 = float(user_input_list[2])

        #string  has an operatero num1 and num2

        #if token 0 is equal to "operator"
             #call the function for operator and use num1 and num2 as arguments
        if user_input_list[0] == "+":
            print(add(num1 , num2))

        elif user_input_list[0] == "-":
            print(subtract(num1 , num2))

        elif user_input_list[0] == "*":
            print(multiply(num1 , num2))   

        elif user_input_list[0] == "/":
            print(divide(num1, num2))

        elif user_input_list[0] == "square":
            print(square(num1, num2))

        elif user_input_list[0] == "cube":
            print(cube(num1, num2))

        elif user_input_list[0] == "pow":
            print(power(num1, num2))

        elif user_input_list[0] == "mod":
            print(mod(num1, num2))


