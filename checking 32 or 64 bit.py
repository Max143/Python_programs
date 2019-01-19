"""
write a python program to find the type of system is.
For 32 bit it will return 32
and for 64 bit it return 64

"""

import struct

print(struct.calcsize("P")*8)

