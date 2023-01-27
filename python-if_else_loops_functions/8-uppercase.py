#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        chars = ord(char)
        if chars >= 97 and chars <= 122:
            upper_str += chr(chars - 32)
        else:
            upper_str += char
    print("{}".format(upper_str))
