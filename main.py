#!/usr/bin/env python3
import sys
import os
import re

if not os.path.exists("./pokeemerald"):
    print("Ya done lost the whole-ass game!")
    exit("oop")

if not os.path.exists("./output/"):
    os.makedirs("./output/")

if len(sys.argv) < 2:
    print("Eyyo you need to specify the file to extract from!")
    exit("whoops!")


def setOutput(toOut):
    toOut = "./output" + sys.argv[1][1:] + "/" + toOut
    return toOut

"""
for i in range(len(sys.argv)):
    if sys.argv[i] == "-D":
        directoryMode = True
    else: directoryMode = False
    

if not directoryMode:
    file = open(sys.argv[1],"r")

    outName = sys.argv[1]
    for i in range(len(outName)):
        if outName[i] == "\\" or outName[i] == "/":
            toDeleteIndex = i
    outName = ".\\output" + outName[toDeleteIndex:]
    print(outName)
    fout = open(outName,"w")
"""

dir = os.listdir(sys.argv[1])

if not os.path.exists("./output" + sys.argv[1]):
    os.makedirs("./output" + sys.argv[1])

for i in range(len(dir)):
    file = open("."+sys.argv[1][1:]+"/"+dir[i],"r",encoding='utf8')
    outName = setOutput(dir[i])
    print(outName)
    fout = open(outName,"w",encoding='utf8')

    readChar = "ass"
    transcribe = False
    escape = False
    escaped = False
    
    while readChar != "":
        readChar = file.read(1)
        
        #escape handling
        if transcribe and escape:
            if readChar == "p":
                fout.write("\n")
            if readChar == "l" or readChar == "n":
                fout.write(" ")
            escaped = True
        
        if transcribe and readChar == "$":
            fout.write("\n")
        
        if transcribe and not escaped and readChar != "\"" and readChar != "$" and (not escape and readChar != "\\"):
            fout.write(readChar)        
        
        if readChar == "\\":
            escape = True
    
        if not escape and readChar == "\"":
            transcribe = not transcribe
        
        if escaped:
            escape = False
            escaped = False
    
