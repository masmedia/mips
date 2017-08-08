#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
import formats 
import functions
from prediction import branch_prediction
from complement import complemented

def type_j(j_ty, coun, memo):
#j_ty=raw_input("ins:")     #These lines are for testing purposes
#coun = 1
#memo = 0x00400020
#for temporar in range(1,2):

#Getting the opcode from dictionary
    counter_j = coun
    memory_j = memo
    j_inst = j_ty                     #entered string
    j_inst = j_inst.replace("$","&")
    j_inst = j_inst.split("&")
    #print j_inst, memory_j

    if (j_inst[0] in opc.keys()[28:]) or (j_inst[1] in opc.keys()[28:]):
        if j_inst[0] in opc.keys()[28:]:
            
            predic = branch_prediction(j_inst[1], counter_j) + 1     #Branch Prediction
            
            memory_j = memory_j + (predic*4)
            print "Jump Memory Location:", hex(memory_j)
            memory_j = (memory_j>>2)
            print "Shifted by 2 bits:", hex(memory_j)
            print opc.get(j_inst[0]),format(memory_j, 'b').zfill(26)
            f = open('mips.obj', 'a')
            list_d=[opc.get(j_inst[0]),format(memory_j, 'b').zfill(26),'\n']
            f.writelines(list_d)
            f.close()
        else:
            
            predic = branch_prediction(j_inst[2], counter_j) + 1     #Branch Prediction
            
            memory_j = memory_j + (predic*4)
            print "Jump Memory Location:", hex(memory_j)
            memory_j = (memory_j>>2)
            print "Shifted by 2 bits:", hex(memory_j)
            print opc.get(j_inst[1]),format(memory_j, 'b').zfill(26)
            f = open('mips.obj', 'a')
            list_d=[opc.get(j_inst[1]),format(memory_j, 'b').zfill(26),'\n']
            f.writelines(list_d)
            f.close()
#The algorithms is same as r and i type instructions except
#the branch prediction is done and depending on the branch prediction
#the memory address calculated in addition to shifting the memory
#address by 2 bits right since hardware appends 2 bits again to the
#instruction




