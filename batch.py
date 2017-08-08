#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from rearrange import rearranger
from functions import op_functs
from formats import mnem
from complement import complemented
from prediction import branch_prediction
from rowno import rowAndOccurrence
from type_r import type_r
from type_i import type_i
from type_j import type_j
from pseudo import pse
from mipseudo import mipseudo

mipsFile = open("mips.src","r")
counter = 0
mem_addr = 0x00400000
rearranger()    #Create the arranged source file for eliminating whitespaces
mipsFile2 = open("mips2.src", "r")  #New source file generated.

for iteration in mipsFile2:         #Checking the mips2.src source file
    counter = counter+1             #for instructions
    print "\nMemory:",format(mem_addr, '02x').zfill(8),"\tInstruction:",counter
    print iteration                 #Printing out the current instruction
                                    #being handled
    instruct = iteration.strip()    #The right and left empty spaces deleted
    instruct = instruct.replace(":",":$")   #Change ':' sign with ':$'
    instruct = instruct.replace(" ","$")    #Change ' ' with '$'
    instruct = instruct.replace(" ","")     #Change ' ' with '' (Extra step)
    instruct = instruct.replace(",","$")    #Change ',' with '$'
    instruct1 = instruct.replace("(","$")   #Change '(' with '$'
    instruct1 = instruct1.replace(")","$")  #Change ')' with '$'
    instruct = instruct.split("$")          #Separate instruction from '$' signs
    instruct = filter(lambda p: p!='', instruct) #Eliminating '' characters
#Now raw instruction string is processed for checking the opcodes inside the dictionary        
    if ((instruct[0]) in mnem.keys()) or ((instruct[1]) in mnem.keys()):
        if (mnem.get(instruct[0]) == 'R'):   #Checking the opcode in dictionary
            type_r(instruct1)                #If a label exitst before the instruction
        elif (mnem.get(instruct[1]) == 'R'): #the opcode will be in the next element
            type_r(instruct1)
            
        elif (mnem.get(instruct[0]) == 'I'): #Checking i and j type instructions
            type_i(instruct1, counter)
            
        elif (mnem.get(instruct[1]) == 'I'):
            type_i(instruct1, counter)
        
        elif mnem.get(instruct[0]) == 'J':
            type_j(instruct1, counter, mem_addr)
            
        elif mnem.get(instruct[1]) == 'J':
            type_j(instruct1, counter, mem_addr)

        else:
            pass    
#If the opcode is not in the original instructions, check the pseudo-instructions        
    elif (instruct[0]in pse.keys()) or (instruct[1]in pse.keys()):
        instruct1 = instruct1.replace("$","&")  #As before these steps are for 
        instruct1 = instruct1.split("&")        #eliminating and processing the string
        instruct1 = filter(lambda m: m!='&',instruct1)
        instruct1 = filter(lambda m: m!='',instruct1)
        if len(instruct1) < 4:      #move and li instructions are shorter than the others
            arg=0   #Passing the arguments to the "mipseudo" function
            mipseudo(instruct1[0],instruct1[1],instruct1[2],arg, counter, mem_addr)
        else:
            mipseudo(instruct1[0],instruct1[1],instruct1[2],instruct1[3], counter, mem_addr)
            

    
    else:
        print "There is no such instruction!!!!!"
    mem_addr += 4


mipsFile.close()
#These instructions almost similar in the interactive mode except from loop
