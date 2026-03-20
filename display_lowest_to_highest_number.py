#Prog04: Create a program that ask user to input a number, continue asking until the user
#input is invalid. Display the number from highest to lowest. Clue: sort() function

numbers = []
while True:
    val = input("Enter a number (or any letter to stop): ")
    try:
        numbers.append(int(val))
    except ValueError:
        break

numbers.sort(reverse=True)
print("Numbers from highest to lowest:", numbers)