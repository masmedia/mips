#!/usr/bin/env python

def rearranger():
#a_string = raw_input("Enter a string:")
#for indices in range(1,2):

    file1 = open("mips.src","r")
    file2 = open("mips2.src", "w")
    newLine = '\n'
    
    
    for filerange in file1:
        a_string = filerange
        arran = a_string.strip()
        file2.writelines(arran)
        file2.writelines(newLine)

        
    

#This module just deletes the empty spaces just in case
#It iterates the line by line and copies the same instructions
#from "mips.src" file to "mips2.src" file. Normally this option
#i.e:           swap: addi $t0, $t1, -4   becomes
#swap: addi $t0, $t1, -4
