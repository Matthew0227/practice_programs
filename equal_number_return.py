# Create a program that ask user to input 2 numbers. Print the bigger number.
def equal_num_return(num1, num2):
    if num1 < num2:
        print(f"these numbers are not equal ({num1}, {num2})")
    elif num2 < num1:
        print(f"these numbers are not equal ({num1}, {num2})")
    else:
        print("the two numbers are equal")
        return num1

def input_user(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            int(num)
            return num
        else:
            print("please input a number")

print("telling if two numbers are equal")

while True:
    number_1 = input_user("Please enter the first number: ")
    number_2 = input_user("Please enter the second number: ")

    equal_num_return(number_1, number_2)

    retry = input("would you like to try again? (y/n): ")
    retry = retry.lower()

    if retry == "n":
        break
