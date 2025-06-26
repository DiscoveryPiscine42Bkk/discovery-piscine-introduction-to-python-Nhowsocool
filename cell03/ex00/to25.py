number = input("Enter a number lees than 25: ")
number = int(number)
if number > 25:
    print("Error")
else:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1