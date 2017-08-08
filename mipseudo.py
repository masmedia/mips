#!/usr/bin/env python
#Driver function of the pseudo-mips functions
from collections import OrderedDict
from type_r import type_r
from type_i import type_i
from type_j import type_j
from registers import reg
from opcodes import opc
from formats import mnem
from functions import op_functs
from complement import complemented
from prediction import branch_prediction
from pseudo import pse
from rowno import rowAndOccurrence

def mipseudo(pseu_inst, arg_zero, arg_one, arg_two, coun, mem):
#pseu_inst = raw_input("Enter the pseudo-instruction:")
#arg_zero = raw_input("Argument0:")
#arg_one = raw_input("Argument1:")
#arg_two = raw_input("Argument2:")
#coun = 25
#mem = 0x00400030
#for temporary in range(1,2):
#The previous lines are for testing purposes
    keyValue = pse.get(pseu_inst)
#The '#' signs added for readability and for visually separating the fields
##################################################################
    if pseu_inst in pse.keys()[0:1]:        #move
#Check the instruction in pseudo keys.         
        for repeat in range(len(keyValue)):    
            newInstruct = keyValue[repeat] +"$"+ arg_zero +"$"+ arg_one +"$"+ "zero"
            type_r(newInstruct)
##################################################################
    elif pseu_inst in pse.keys()[1:2]:      #multi
        
        for repeat in range(len(keyValue)):
            if mnem.get(keyValue[repeat]) == 'R':
                newInstruct = keyValue[repeat] +"$"+ arg_zero +"$"+ arg_one
                type_r(newInstruct)
            else:
                newInstruct = keyValue[repeat] +"$"+ arg_one +"$"+ "zero" +"$"+ arg_two
                coun += repeat
                type_i(newInstruct, coun)
##################################################################
    elif pseu_inst in pse.keys()[2:3]:      #li
        
        for repeat in range(len(keyValue)):
            newInstruct = keyValue[repeat] +"$"+ arg_zero +"$"+ "zero" +"$"+ arg_one
            coun += repeat
            type_i(newInstruct, coun)
            
##################################################################
#Using assembler temporary register    
    elif pseu_inst in pse.keys()[3:]:      #blt, ble, bgt, bge
        
        for repeat in range(len(keyValue)):
            if mnem.get(keyValue[repeat]) == 'R':
                newInstruct = keyValue[repeat] +"$"+ "at" +"$"+ arg_zero +"$"+ arg_one
                type_r(newInstruct)
            else:
                newInstruct = keyValue[repeat] +"$"+ "at" +"$"+ arg_zero +"$"+ arg_two
                coun += repeat
                type_i(newInstruct, coun)
            
##################################################################
        
    else:
        pass

#The instructions are all in for loops. It iterates till the dictionary value length.
#If the dictionary key contains more than one value, it makes use of
#iterating them one by one and checks the types whether they are in R or I type. 
#Since each of these pseudo-instructions can be transformed into the real instructions,
#the code checks them and depending on the type, it transforms the pseudo instruction
#opcodes to real instruction opcodes and rearranges the arguments of them then calls
#the r_type or i_type modules to handle them


    
