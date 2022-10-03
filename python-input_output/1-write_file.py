#!/usr/bin/python3
"""Write to a file"""
def write_file(filename="", text=""):
    """ function that writes a string to a text file"""
    with open("filename", mode="w", encoding="utf-8") as myFile:
        return(myFile.write(text))
        