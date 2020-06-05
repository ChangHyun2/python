import sys

try:
    x = int(input('x: '))
    y = int(input('x: '))
except ValueError:
    print("Error: invalid Input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: cannot divide by 0.")
    sys.exit(1) # status code 1 : something with wrong
print(f"{x}/{y} = : {result}")
 