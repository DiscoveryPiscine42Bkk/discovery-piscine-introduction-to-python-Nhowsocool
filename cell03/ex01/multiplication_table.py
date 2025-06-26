number = input("Enter a number: ")
number = int(number)
i = 0
while i <= 10:
    result = i * number
    print(f'{i} X {number} = {result}')
    i += 1