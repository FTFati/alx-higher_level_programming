#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    for i in roman_string:
        if (i != 'I' and i != 'V' and i != 'X' and
                i != 'L' and i != 'C' and i != 'D' and i != 'M'):
            return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = []
    for j in range(len(roman_string) - 1, -1, -1):
        if j == len(roman_string) - 1:
            largestNum = rom_num[roman_string[j]]
        if rom_num[roman_string[j]] < largestNum:
            num.append(largestNum - rom_num[roman_string[j]])
            num.remove(largestNum)
            largestNum = rom_num[roman_string[j]]
        else:
            num.append(rom_num[roman_string[j]])
            largestNum = rom_num[roman_string[j]]
    return sum(num)
