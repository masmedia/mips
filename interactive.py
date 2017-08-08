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

#Counter and mem_addr variables are put for testing purposes
#If they do not exist i_type and j_type functions gives error
counter = 40
mem_addr = 0x00400000
rearranger()        #Create the arranged source file
instruct = raw_input("Please enter the MIPS instruction:")
#The lines are 
for iteration in range(1,2):    #This for loop is for testing purpose
    counter = counter+1         #It iterates only once
#These instruction are the same as batch mode and explained there    
    instruct = instruct.strip()
    instruct = instruct.replace(":",":$")
    instruct = instruct.replace(" ","$")
    instruct = instruct.replace(" ","")
    instruct = instruct.replace(",","$")
    instruct1 = instruct.replace("(","$")
    instruct1 = instruct1.replace(")","$")
    instruct = instruct.split("$")
    instruct = filter(lambda p: p!='', instruct)
    
    if ((instruct[0]) in mnem.keys()) or ((instruct[1]) in mnem.keys()):
        if (mnem.get(instruct[0]) == 'R'):
            type_r(instruct1)
        elif (mnem.get(instruct[1]) == 'R'):
            type_r(instruct1)
            
        elif (mnem.get(instruct[0]) == 'I'):
            type_i(instruct1, counter)
            
        elif (mnem.get(instruct[1]) == 'I'):
            type_i(instruct1, counter)
        
        elif mnem.get(instruct[0]) == 'J':
            type_j(instruct1, counter, mem_addr)
            
        elif mnem.get(instruct[1]) == 'J':
            type_j(instruct1, counter, mem_addr)
        else:
            pass
    elif (instruct[0]in pse.keys()) or (instruct[1]in pse.keys()):
        instruct1 = instruct1.replace("$","&")
        instruct1 = instruct1.split("&")
        instruct1 = filter(lambda m: m!='&',instruct1)
        instruct1 = filter(lambda m: m!='',instruct1)
        if len(instruct1) < 4:
            arg=0
            mipseudo(instruct1[0],instruct1[1],instruct1[2],arg, counter, mem_addr)
        else:
            mipseudo(instruct1[0],instruct1[1],instruct1[2],instruct1[3], counter, mem_addr)
            
    else:
        print "There is no such instruction!!!!!"
    mem_addr += 4


