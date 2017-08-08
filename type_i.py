#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
from prediction import branch_prediction
from rowno import rowAndOccurrence
import formats 
import functions
from complement import complemented

def type_i(i_ty, coun):
#coun = 40
#i_ty=raw_input("ins:")
#for temporar in range(1,2):

#Getting the opcode from dictionary
    i_inst = i_ty                       #Entered string
    i_inst = i_inst.replace("$","&")    #Rearrange $ signed places
    i_inst = i_inst.split("&")          #Split them from & signs
    i_inst = filter(lambda q: q!='&', i_inst) #Filter '&' characters
    i_inst = filter(lambda q: q!='', i_inst)  #Filter '' characters

#opcode check
    #addi, andi, ori, slti, sltiu
    if (i_inst[0] in opc.keys()[10:15]) or (i_inst[1] in opc.keys()[10:15]):  
        if i_inst[0] in opc.keys()[10:15]:      #Check for opcodes in dictionary
            h=int(i_inst[3])                    #Convert it to integer
            h = complemented(h, 16)             #Complemet the constant
#If the constant is +ve, it does nothing, else complements
            print opc.get(i_inst[0]),reg.get(i_inst[2]),reg.get(i_inst[1]),h
            f = open('mips.obj', 'a')
            list_a=[opc.get(i_inst[0]),reg.get(i_inst[2]),reg.get(i_inst[1]),h,'\n']
            f.writelines(list_a)        #Write the string into file:"mips.obj"
            f.close() 
        else:
            h=int(i_inst[4])                    #Convert it to integer
            h = complemented(h, 16)
            
            print opc.get(i_inst[1]),reg.get(i_inst[3]),reg.get(i_inst[2]),h
            f = open('mips.obj', 'a')
            list_a=[opc.get(i_inst[1]),reg.get(i_inst[3]),reg.get(i_inst[2]),h,'\n']
            f.writelines(list_a)
            f.close()
#####################################################################
    elif (i_inst[0] in opc.keys()[15:26]) or (i_inst[1] in opc.keys()[15:26]):
        if i_inst[0] in opc.keys()[15:26]:
            h=int(i_inst[2])                    #Convert it to integer
            h = complemented(h, 16)
            
            print opc.get(i_inst[0]),reg.get(i_inst[3]),reg.get(i_inst[1]),h
            f = open('mips.obj', 'a')
            list_b=[opc.get(i_inst[0]),reg.get(i_inst[3]),reg.get(i_inst[1]),h,'\n']
            f.writelines(list_b)
            f.close()
        else:
            h=int(i_inst[3])                    #Convert it to integer
            h = complemented(h, 16)
            
            print opc.get(i_inst[1]),reg.get(i_inst[4]),reg.get(i_inst[2]),h
            f = open('mips.obj', 'a')
            list_b=[opc.get(i_inst[1]),reg.get(i_inst[4]),reg.get(i_inst[2]),h,'\n']
            f.writelines(list_b)
            f.close()
#####################################################################
    elif (i_inst[0] in opc.keys()[26:28]) or (i_inst[1] in opc.keys()[26:28]):
        if i_inst[0] in opc.keys()[26:28]:
            h = i_inst[3]
            last_field = branch_prediction(h, coun)     #Branch Prediction
            print "Branch Prediction:", last_field
            last_field = complemented(last_field, 16)
            
            print opc.get(i_inst[0]),reg.get(i_inst[1]),reg.get(i_inst[2]),last_field
            f = open('mips.obj', 'a')
            list_c=[opc.get(i_inst[0]),reg.get(i_inst[1]),reg.get(i_inst[2]),last_field,'\n']
            f.writelines(list_c)
            f.close()
        else:
            h = i_inst[4] 
            last_field = branch_prediction(h, coun)
            print "Branch Prediction:", last_field
            last_field = complemented(last_field, 16)
            
            print opc.get(i_inst[1]),reg.get(i_inst[2]),reg.get(i_inst[3]),last_field
            f = open('mips.obj', 'a')
            list_c=[opc.get(i_inst[1]),reg.get(i_inst[2]),reg.get(i_inst[3]),last_field,'\n']
            f.writelines(list_c)
            f.close()
            
#####################################################################
#Since the lines are long, some of the comments and algorithm is written here
#First the passed string is still in raw form,  replace '$' signs with
#'&' sign since it never occurs in the mips instructions. Then decompose
#the string and filter certain characters them such as ''. Then check the opcodes
#in the dictionary. If the opcode is in the dictionary, the corresponding fields are
# written into the "mips.obj" file.
###.... fields are for visual purposes for checking the separate instructions.
