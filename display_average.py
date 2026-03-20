#Prog05: Create a program that ask user to input a number, continue asking until the user
#input is invalid. Display the average.

numbers = []
while True:
    val = input("Enter a number (or any letter to stop): ")
    try:
        numbers.append(int(val))
    except ValueError:
        break

if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"The average is: {avg}")
    