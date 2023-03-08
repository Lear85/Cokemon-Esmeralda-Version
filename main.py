#!/usr/bin/env python3
import sys
import os
import re

if not os.path.exists("./pokeemerald"):
    print("Ya done lost the whole-ass game!")
    exit("oop")

os.makedirs("output", exist_ok=True)

if len(sys.argv) < 2:
    print("Eyyo you need to specify the file to extract from!")
    exit("whoops!")

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

for filename in os.listdir(sys.argv[1]):
    path = os.path.join(sys.argv[1], filename)
    if not os.path.isfile(path):
        print("This shit is not a file, fuck you: " + path)
        continue
    outPath = os.path.join("output", path)
    outDir = os.path.dirname(outPath)
    os.makedirs(outDir, exist_ok=True)

    file = open(path, "r", encoding="utf8")
    fout = open(outPath, "w", encoding="utf8")

    transcribe = False
    escape = False
    escaped = False
    
    while readChar := file.read(1):
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
    
    # TODO: Have Claire restart her computer
