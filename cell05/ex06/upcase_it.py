#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    new = [x.upper() for x in sys.argv]
    print(new)
else:
    print("none")