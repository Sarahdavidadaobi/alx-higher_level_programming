#!/usr/bin/python3
for letter_code in range(ord('a'), ord('z') + 1):
    if chr(letter_code) not in ('q', 'e'):
        print(chr(letter_code), end='')
