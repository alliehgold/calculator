import sys


'''
This program will add, subtract, multiply, or divide based on user input.

It will first ask the user which option they would like, followed by asking them to enter two numbers.

It will then perform the specified calulation with the two given numbers
'''


#This function will get the two numbers from the user
def get_numbers():
    #This will attempt to get the input and convert to a float.
    #It will return an error and exit if the user did not enter two numbers
    try:
        num_1 = float(input("Please enter the first number:\n"))
        num_2 = float(input("Please enter the second number:\n"))
    except:
        print("Error: Invalid Numbers entered")
        sys.exit()

    #This will test if the inputs are integers or floats and return the values accordingly
    if num_1.is_integer() and num_2.is_integer():
         return int(num_1), int(num_2)
    else:
         return num_1, num_2
    

user_continue = True
    
#Allows the user to run calculations multiple times
while user_continue:

    #Getting which operator the user would like
    user_choice = input("Please enter one of the following choices:" \
    "\n1. Add" \
    "\n2. Subtract" \
    "\n3. Multiply" \
    "\n4. Divide\n")

    
    is_valid_input = False

    #This iterates to test if the user selected one of the valid options
    #This allows for expansion when more expressions are added later
    for i in range (1, 5):
        if i == int(user_choice):
            is_valid_input = True


    #This will run the correct operation if the input is valid
    #Each operation will also check if the result is in integer or float, and will print the value accordingly
    #While this is not entirely necessary, it helps with readability.
    if is_valid_input:
        operands = get_numbers()
        if user_choice =="1":
                total = operands[0] + operands[1]
                if total.is_integer():
                    total = int(total)
                print(f"{operands[0]} + {operands[1]} = {total}")

        elif user_choice == "2":
            total = operands[0] - operands[1]
            if total.is_integer():
                    total = int(total)
            print(f"{operands[0]} - {operands[1]} = {total}")

        elif user_choice == "3":
            total = operands[0] * operands[1]
            if total.is_integer():
                    total = int(total)
            print(f"{operands[0]} * {operands[1]} = {total}")

        elif user_choice == "4":
            total = operands[0] / operands[1]
            if total.is_integer():
                    total = int(total)
            print(f"{operands[0]} / {operands[1]} = {total}")
        
    else:
         print("That is not a valid option")

    continue_choice = input("Press 'y' to perform another operation, or any other key to exit:\n")

    if continue_choice != "y":
         user_continue = False

sys.exit()