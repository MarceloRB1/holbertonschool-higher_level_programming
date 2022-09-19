#!/usr/bin/python3
def get_symbol(i):
        if (i == 'I'):
            return 1
        if (i == 'V'):
            return 5
        if (i == 'X'):
            return 10
        if (i == 'L'):
            return 50
        if (i == 'C'):
            return 100
        if (i == 'D'):
            return 500
        if (i == 'M'):
            return 1000
        return -1


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    x = 0
    y = len(roman_string)

    while (x < y):
        symbol1 = get_symbol(roman_string[x])
        if (x + 1 < y):
            symbol2 = get_symbol(roman_string[x + 1])

            if (symbol1 >= symbol2):
                total = total + symbol1
                x = x + 1
            else:
                total = total + symbol2 - symbol1
                x = x + 2
        else:
            total = total + symbol1
            x = x + 1
    return total
