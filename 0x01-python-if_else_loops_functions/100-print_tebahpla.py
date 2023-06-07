#!/usr/bin/python3
# 100-print_tebahpla.py

x = 0
for m in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(m - x)), end="")
    x = 32 if x == 0 else 0
