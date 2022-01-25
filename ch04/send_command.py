#!/usr/bin/env python3.9

import sys

if __name__ == "__main__":
    args = sys.argv
    print(sys.argv)
    print("Username:  " + args[0])
    print("Password:  " + args[1])
    print("Device IP: " + args[2])
    print("Command:   " + args[3])