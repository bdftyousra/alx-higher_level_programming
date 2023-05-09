#!/usr/bin/python3

for x in range(0, 10):
    for y in range(x + 1, 10):
        if (not (x == 8 and y == 9)):
            print("{}{}".format(x, y), end=", ")
        else:
            print("{}{}".format(x, y))
