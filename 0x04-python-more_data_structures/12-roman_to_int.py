#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        raise ValueError("Empty string is not a valid Roman numeral")

    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        current_value = roman_nums[roman_string[i]]
        next_value = roman_nums[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

        if current_value < next_value:
            total -= current_value
        else:
            total += current_value

    return total

