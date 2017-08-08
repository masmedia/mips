#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
import formats 
import functions

def rowAndOccurrence(a_string):
    in_str = a_string
    oldFiles = open("mips2.src", "r")
    
    numlines = 0    #Number of the line in source file
    prev_found = 0  #These variables are for comparison of lines
    found = 0       
    inst_number= 0
    order = []      #Array for occurrences of the label string

    for line in oldFiles: #Check for 
        numlines += 1     #Increment the line in file being searched
        found += line.count(in_str) 
        if line =='\n':   #If there exists whitespace, discard
            numlines -=1
        if prev_found != found:     
            order.append(numlines)  #Store the number of occurrences
            prev_found +=1          #in an array.
    oldFiles.close()
    return order
#This module checks for the label that is going to be the
#branch address with respect to the caller function.
#It counts the line of the "label:" field in file and returns
#the line that is occur in the code.
