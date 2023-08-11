#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    names = dir(hidden_4)[-3:]
    for i in range(0, len(names)):
        print(names[i])
