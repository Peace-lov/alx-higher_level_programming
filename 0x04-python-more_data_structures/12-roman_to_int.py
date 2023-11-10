#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_n = 0
    for a in range(len(roman_string)):
        if a > 0 and rom_d[roman_string[a]] > rom_d[roman_string[a - 1]]:
            rom_n += rom_d[roman_string[a]] - 2 * \
                    rom_d[roman_string[a - 1]]
        else:
            rom_n += rom_d[roman_string[a]]
    return rom_n
