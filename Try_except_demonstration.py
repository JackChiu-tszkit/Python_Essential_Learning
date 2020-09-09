#!/usr/bin/python
# -*- coding: UTF-8 -*-


try:
    fh = open("testfile", "w")
    fh.write("This is a test file!!")
finally:
    print("Error: Failure to load the file")

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is a test file")
    finally:
        print("close file")
        fh.close()
except Error:
    print("Error: Failure to load the file")


def temp_convert(var):
    try:
        return int(var)

    except ValueError as Argument:
        print("The parameter does not contain any numbers\n", Argument)


# 调用函数
temp_convert("xyz");