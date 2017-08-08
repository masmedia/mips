#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
import formats 
import functions
from rowno import rowAndOccurrence

#inputted = raw_input("Gir:")   #These lines are used for testing purposes
#ckntr = 7
def branch_prediction(inputted, ckn):
        ckntr = ckn
        input_str = inputted
        newStr = inputted +":"  #Add ':' term to the label and check

        forum = rowAndOccurrence(newStr)  #Send the line of the 
        oldFile = open("mips2.src", "r")
        numlines1=0
        prev_found1=0
        found1=0
        order1=[]
        for line in oldFile:    #Check for mips2.src 
                numlines1 += 1
                found1 += line.count(newStr)
                if line =='\n':
                    numlines1 -= 1
                if prev_found1 != found1:
                    order1.append(numlines1)  #Store the number of occurrences
                    prev_found1 += 1

        oldFile.close()
        orum = order1

        if ckntr > order1[0]:
                result = -(ckntr - order1[0]+1)
        else:
                result = order1[0]-ckntr -1
        #print "Branch Prediction:", result
        return result
#This module counts the branch calling function's label field in the file. Then it
#calls the "rowAndOccurrence() function. That returns the branching line.
#Since the 'label' in branch instruction ("bne $t0, $t1, swap") is also occur
#in the branch address label (i.e:"swap:"), we have to check for ":" added label
#in rowAndOccurrence() function. If the lines are equal, discard, else calculate
#the branch distance with respect to caller.
