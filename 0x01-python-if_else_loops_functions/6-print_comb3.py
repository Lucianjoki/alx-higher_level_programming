#!/usr/bin/python3
for i in range(9):
    for k in range(i+1, 10):
        if i * 10 + k < 89:
            print("{:d}{:d}".format(i, k), end=", ")
print("{:d}".format(89))
