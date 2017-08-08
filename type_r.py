#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
import formats 
from functions import op_functs

#This module responsible of implementing R-type instructions
#It is by default, a function driven by batch or interactive mode modules
#To check the execution of this module itself, add '#' sign before to the
#"def type_r(r_ty):" line to disable it as a comment line. Then delete the '#'
#sign from the next two lines to enable them

def type_r(r_ty):
#r_ty=raw_input("ins:")
#for temporar in range(1,2):
    
    
#Getting the opcode from dictionary
    r_inst = r_ty.replace("$","&")
    #print r_inst, "Typ:",type(r_inst)

    r_inst = r_inst.split("&")                       #Entered string
    r_inst = filter(lambda q: q!='&', r_inst)
    r_inst = filter(lambda q: q!='', r_inst)

    #print r_inst
   # print r_inst[0], r_inst[1], r_inst[2], r_inst[3]
    
    
#Opcode check

    if (r_inst[0] in opc.keys()[0:6]) or (r_inst[1] in opc.keys()[0:6]):  #add, sub, and, or, nor, slt
        shamt="00000"
        if (r_inst[0] in opc.keys()[0:6]):
            print opc.get(r_inst[0]),reg.get(r_inst[2]),reg.get(r_inst[3]),reg.get(r_inst[1]),shamt,op_functs.get(r_inst[0])
            f = open('mips.obj', 'a')
            list_a=[opc.get(r_inst[0]),reg.get(r_inst[2]),reg.get(r_inst[3]),reg.get(r_inst[1]),shamt,op_functs.get(r_inst[0]),'\n']
            f.writelines(list_a)
            f.close()
        
        else:
            print opc.get(r_inst[1]),reg.get(r_inst[3]),reg.get(r_inst[4]),reg.get(r_inst[2]),shamt,op_functs.get(r_inst[1])
            f = open('mips.obj', 'a')
            list_a=[opc.get(r_inst[1]),reg.get(r_inst[3]),reg.get(r_inst[4]),reg.get(r_inst[2]),shamt,op_functs.get(r_inst[1]),'\n']
            f.writelines(list_a)
            f.close()
###########################################################################
    elif (r_inst[0] in opc.keys()[6:8]) or (r_inst[1] in opc.keys()[6:8]): #srl, sll
        rs_p="00000"
        if (r_inst[0] in opc.keys()[6:8]):
            shamt = int(r_inst[3])
            if (shamt <0) or (shamt>32):
                print "It cannot be shifted that amount!"
            else:
                print opc.get(r_inst[0]),rs_p,reg.get(r_inst[2]),reg.get(r_inst[1]),format(shamt,'b').zfill(5),op_functs.get(r_inst[0])
                f = open('mips.obj', 'a')
                list_b=[opc.get(r_inst[0]),rs_p,reg.get(r_inst[2]),reg.get(r_inst[1]),format(shamt,'b').zfill(5),op_functs.get(r_inst[0]),'\n']
                f.writelines(list_b)
                f.close()
        else:
            shamt = int(r_inst[4])
            if (shamt <0) or (shamt>32):
                print "It cannot be shifted that amount!"
            else:
                print opc.get(r_inst[1]),rs_p,reg.get(r_inst[3]),reg.get(r_inst[2]),format(shamt,'b').zfill(5),op_functs.get(r_inst[1])
                f = open('mips.obj', 'a')
                list_b=[opc.get(r_inst[1]),rs_p,reg.get(r_inst[3]),reg.get(r_inst[2]),format(shamt,'b').zfill(5),op_functs.get(r_inst[1]),'\n']
                f.writelines(list_b)
                f.close()
###########################################################################
    elif (r_inst[0] in opc.keys()[8:9]) or (r_inst[1] in opc.keys()[8:9]):   #jr
        rs_r="000000000000000"
        if r_inst[0] in opc.keys()[8:9]:
            print opc.get(r_inst[0]),reg.get(r_inst[1]),rs_r,op_functs.get(r_inst[0])
            f = open('mips.obj', 'a')
            list_c=[opc.get(r_inst[0]),reg.get(r_inst[1]),rs_r,op_functs.get(r_inst[0]),'\n']
            f.writelines(list_c)
            f.close()
        else:
            print opc.get(r_inst[1]),reg.get(r_inst[2]),rs_r,op_functs.get(r_inst[1])
            f = open('mips.obj', 'a')
            list_c=[opc.get(r_inst[1]),reg.get(r_inst[2]),rs_r,op_functs.get(r_inst[1]),'\n']
            f.writelines(list_c)
            f.close()

###########################################################################
    elif (r_inst[0] in opc.keys()[9:10]) or (r_inst[1] in opc.keys()[9:10]):   #mult
        rs_r="0000000000"
        if r_inst[0] in opc.keys()[9:10]:
            print opc.get(r_inst[0]),reg.get(r_inst[1]),reg.get(r_inst[2]),rs_r,op_functs.get(r_inst[0])
            f = open('mips.obj', 'a')
            list_c=[opc.get(r_inst[0]),reg.get(r_inst[1]),reg.get(r_inst[2]),rs_r,op_functs.get(r_inst[0]),'\n']
            f.writelines(list_c)
            f.close()
        else:
            print opc.get(r_inst[1]),reg.get(r_inst[2]),reg.get(r_inst[3]),rs_r,op_functs.get(r_inst[1])
            f = open('mips.obj', 'a')
            list_c=[opc.get(r_inst[1]),reg.get(r_inst[2]),reg.get(r_inst[3]),rs_r,op_functs.get(r_inst[1]),'\n']
            f.writelines(list_c)
            f.close()

                
    else:
        pass
