# Create a program that ask user to input 2 numbers. Print the bigger number.
def lowest_picker(num1, num2):
    if num1 < num2:
        return num1
    elif num2 < num1:
        return num2
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

print("Lowest number picker between two numbers")

while True:
    number_1 = input_user("Please enter the first number: ")
    number_2 = input_user("Please enter the second number: ")

    lowest_num = lowest_picker(number_1, number_2)

    print(f"the lowest number is '{lowest_num}'")

    retry = input("would you like to try again? (y/n): ")
    retry = retry.lower()

    if retry == "n":
        break
