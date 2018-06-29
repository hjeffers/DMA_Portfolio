import sys
import math

def hypotenuse(a, b):  #defining the function
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)
    return math.sqrt (a_squared + b_squared)  #returning the function

def leg(b, c):
    b_squared = math.pow(b, 2)
    c_squared = math.pow(c, 2)
    return math.sqrt (c_squared - b_squared)

def main():
    command = sys.argv[1]

    if command == "add":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x+y)

    if command == "subtract":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x-y)

    if command == "multiply":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x*y)

    if command == "divide":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(x/y)

    if command == "countto":
        x = int(sys.argv[2])
        i = 1
        for i in range(x):
            print (i) + 1

    if command == "power":
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        print(math.pow(x, y))

    if command == "hypotenuse":
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        print (hypotenuse(a, b))  #calling the function

    if command == "leg":
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        print (leg(b, c))

if __name__ == '__main__':
    main()
