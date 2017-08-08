#!/usr/bin/env python
from collections import OrderedDict
from registers import reg
from opcodes import opc
import formats 
import functions

#The three lines below def is for testing purposes
def complemented(num, bit):
#num = int(raw_input("Number:"))
#bit = int(raw_input("Number of bits:"))
#for iterationss in range(1,2):

    if num < 0: 
        num = ( 1<<bit ) + num
    result = '{:0%ib}' % bit
#    print result.format(num)       #For testing purpose
    return result.format(num)

