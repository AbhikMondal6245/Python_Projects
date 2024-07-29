import sys
print("_____CALCULATOR_____")

# try and except is used for error handling
try:
    # after completing the operation, for asking the user to continue with another operation,
    # and take input from user and then as per choice recall the function again using while loop.
    while True:
        # for taking input for the two numbers from user :
        number_1 = float(input("Enter the first number to make an operation: "))
        number_2 = float(input("Enter the second number to make an operation: "))

        # for print the operation names with their assigned integer values :
        print("   ___CAUTION___  ")
        print("Enter 1 for Addition(+) \nEnter 2 for Subtraction(-) \nEnter 3 for Multiplication(*) \nEnter 4 for Division(/) \nEnter 5 for Modulus(%) \nEnter 6 for Exponentiation(**) \nEnter 7 for Floor Division(//)")

        # for taking input for the operation choice from user :
        user_choice = int(input("Put your choice of operation between [1 - 7] here: "))

        # making main function of calculator using if,else condition
        # addition :
        if user_choice == 1:
            print("The Addition(+) of two given number is : ", number_1 + number_2)

        # subtraction :
        elif user_choice == 2:
            print("The Subtraction(-) of two given number is : ", number_1 - number_2)

        # multiplication :
        elif user_choice == 3:
            print("The Multiplication(*) of two given number is : ", number_1 * number_2)

        # division :
        elif user_choice == 4:
            try:
                if number_2 == 0:
                    print("[Cannot divide by 0]")
                    number_2 = float(input("Please enter the second number[should be non-zero] to make this Division: "))
                    if number_2 == 0:
                        print("[Please make another Operation]")
                    else:
                        print("The Division(/) of two given number is : ", number_1 / number_2)
                else:
                    print("The Division(/) of two given number is : ", number_1 / number_2)

            except number_2 != 0:
                print("The Division(/) of two given number is : ", number_1 / number_2)
            else:
                print(" ________________________________________________________________________  ")

        # modulo :
        elif user_choice == 5:
            try:
                if number_2 == 0:
                    print("[Cannot divide by 0]")
                    number_2 = float(input("Please enter the second number[should be non-zero] to make this Modulo Operation: "))
                    if number_2 == 0:
                        print("[Please make another Operation]")
                    else:
                        print("The Modulus(%) of two given number is : ", number_1 % number_2)
                else:
                    print("The Modulus(%) of two given number is : ", number_1 % number_2)

            except number_2 != 0:
                print("The Modulus(%) of two given number is : ", number_1 % number_2)
            else:
                print(" ________________________________________________________________________  ")

        # exponentiation :
        elif user_choice == 6:
            print("The Exponentiation(**) of two given number is : ", number_1 ** number_2)

        # floor division :
        elif user_choice == 7:
            try:
                if number_2 == 0:
                    print("[Cannot divide by 0]")
                    number_2 = float(input("Please enter the second number[should be non-zero] to make this Floor Division(//): "))
                    if number_2 == 0:
                        print("[Please make another Operation]")
                    else:
                        print("The Floor Division(//) of two given number is : ", number_1 // number_2)
                else:
                    print("The Floor Division(//) of two given number is : ", number_1 // number_2)
            except number_2 != 0:
                print("The Floor Division(//) of two given number is : ", number_1 // number_2)
            else:
                print(" ________________________________________________________________________  ")

        else:
            print("[Please Enter a Valid Input]")

        # asking user if user wants to continue with another operation and then take input from user and recall the whole function as per choice
        retask2 = input("Do you want to make another operation [For yes enter Y] , [For no enter N] : ")
        if retask2 == "y" or retask2 == "Y":
            print("[Please select again]")
        elif retask2 == "n" or retask2 == "N":
            print(".....THANK YOU for using CALCULATOR.....")
            break
        else:
            print("[Please select again & enter a Valid Input]")

except:
    sys.exit("Enter values only!")
