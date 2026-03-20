#Prog03: Create a program that ask user to input a number, continue asking until the user
#input is invalid. Display the highest number

highest = None
while True:
    val = input("Enter a number (or any letter to stop): ")
    try:
        num = int(val)
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

print(f"The highest number is: {highest}")