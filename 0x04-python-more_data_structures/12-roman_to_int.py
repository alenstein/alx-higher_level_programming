#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    """Convert a Roman numeral string to an integer.

    Parameters:
    roman_string (str): A Roman numeral string.

    Returns:
    int: The corresponding integer value of the Roman numeral.
    0 if input is not a string or None
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_to_int_d: dict[str, int] = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    for i in range(len(roman_string)):
        if (i > 0 and roman_to_int_d[roman_string[i]]) > \
                roman_to_int_d[roman_string[i-1]]:
            result += roman_to_int_d[roman_string[i]] - 2 *\
                      roman_to_int_d[roman_string[i-1]]
        else:
            result += roman_to_int_d[roman_string[i]]
    return result
