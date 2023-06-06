#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in lowercase, but not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
