#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    first_input = sys.argv[1]
    usr_input = input("What was the parameter")

    if usr_input == first_input:
        print("Good job")
    else:
        print("Nope, sorry")
    