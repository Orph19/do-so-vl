#!/usr/bin/env python3
file = open('t3.txt')

# try:
#     a = 0/0
#     print(a)
# except:
#     print("Seems to be something ocurred, try again")
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")
linux_interaction()
