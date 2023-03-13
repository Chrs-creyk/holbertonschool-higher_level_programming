#!/usr/bin/python3
"""write empty or only lines"""


def number_of_lines(filename=""):
    """function"""
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())
