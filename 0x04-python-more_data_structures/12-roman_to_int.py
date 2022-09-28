#!/usr/bin/python3
def roman_to_int(roman_string):
    decimal = 0
    roman = {}
    roman['I'] = 1
    roman['V'] = 5
    roman['X'] = 10
    roman['L'] = 50
    roman['C'] = 100
    roman['D'] = 500
    roman['M'] = 1000

    if roman_string is None or type(roman_string) != str:
        return 0

    i = 0
    while(i < len(roman_string)):
        if i == len(roman_string) - 1:
            decimal += roman[roman_string[i]]
        elif roman[roman_string[i]] < roman[roman_string[i + 1]]:
            decimal -= roma[roman_string[i]]
        else:
            decimal += roman[roman_string[i]]
    return decimal
