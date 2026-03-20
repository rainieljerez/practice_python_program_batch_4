#Prog02: Create a program that ask user to input a number, continue asking until the
#user input is invalid. Display the number with the most number of duplicate.
numbers = []
while True:
    val = input("Enter a number (or any letter to stop): ")
    if not val.isdigit(): # Check if input is a valid number
        break
    numbers.append(int(val))

if numbers:
    most_frequent = max(set(numbers), key=numbers.count)
    print(f"The number with the most duplicates is: {most_frequent}")