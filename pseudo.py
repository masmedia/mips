#!/usr/bin/env python
from collections import OrderedDict
#Contains formats of the pseudoinstructions

pse=OrderedDict([("move",["add"]),
 ("multi",["addi","mult"]),
 ("li",["ori"]),
 ("blt",["slt","bne"]),
 ("ble",["slt","beq"]),
 ("bgt",["slt","bne"]),
 ("bge",["slt","beq"])])
