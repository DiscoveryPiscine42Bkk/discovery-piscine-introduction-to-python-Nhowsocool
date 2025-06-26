#!/usr/bin/env python3
first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
first_num = int(first_num)
second_num = int(second_num)
result = first_num * second_num
print(result)
if result == 0:
    print("This result is positive and negative")
elif result > 0:
    print("This result is positive")
elif result < 0:
    print("This result is negative")
