#!/usr/bin/env python3
num_array = [2, 8, 9, 48, 8, 22, -12, 2 ]
print(num_array)
new_array = [x+2 for x in num_array if x > 5]
print(set(new_array))
