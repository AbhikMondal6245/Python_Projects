import string
import random
import sys
print("_____PASSWORD GENERATOR_____")


if __name__ == "__main__":  # this allows the program to be executable by itself

    try:  # try and except is used for error handling

        set_1 = string.ascii_uppercase  # for uppercase characters
        set_2 = string.digits  # for digits
        set_3 = string.ascii_lowercase  # for lowercase characters
        set_4 = string.punctuation  # for symbols

        # after completing the operation, for asking the user to continue with another operation,
        # and take input from user and then as per choice recall the function again using while loop.
        while True:

            # for taking the input from the user for password length
            pw_length = int(input("Enter the length of password you want to create : "))

            # for taking the input from the user for password complexity level
            complexity = input("Enter the desired complexity level [Easy/Medium/Hard] : ").lower()
            if complexity == 'easy':
                easy_main_set = []
                easy_main_set.extend(list(set_1))
                easy_main_set.extend(list(set_2))
                # converts set_1 and set_2 into list and assigned to the easy_main_set
                print("Your Password is : ")
                print("".join(random.sample(easy_main_set, pw_length)))
                # from random.sample we get random characters/values from the easy_main_set according to pw_length

            elif complexity == 'medium':
                medium_main_set = []
                medium_main_set.extend(list(set_1))
                medium_main_set.extend(list(set_2))
                medium_main_set.extend(list(set_3))
                # converts set_1, set_2 and set_3 into list and assigned to the medium_main_set
                print("Your Password is : ")
                print("".join(random.sample(medium_main_set, pw_length)))
                # from random.sample we get random characters/values from the medium_main_set according to pw_length

            elif complexity == 'hard':
                hard_main_set = []
                hard_main_set.extend(list(set_1))
                hard_main_set.extend(list(set_2))
                hard_main_set.extend(list(set_3))
                hard_main_set.extend(list(set_4))
                # converts set_1, set_2, set_3 and set_4 into list and assigned to the hard_main_set
                print("Your Password is : ")
                print("".join(random.sample(hard_main_set, pw_length)))
                # from random.sample we get random characters/values from the hard_main_set according to pw_length

            else:
                print("[Please enter a Valid Input]")
                print("[_____Select again to continue_____]")

            # asking user if user wants to continue with other operation and then take input from user
            # and recall the whole function as per choice
            retask = input("Do you want to create another Password? [For yes enter Y] , [For no enter N] : ")
            if retask == "y" or retask == "Y":
                print("[Please select again]")
            elif retask == "n" or retask == "N":
                print(".....THANK YOU for using PASSWORD GENERATOR.....")
                break
            else:
                print("[Please select again & enter a Valid Input]")
    except:
        sys.exit("Enter values only!")
