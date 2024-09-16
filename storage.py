#!/usr/bin/env python3.12

import os

def clear(): os.system('clear')


# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
#foo = [1, 2, 4, 5, 3, 5]
#print(f7(foo))


def one_to_n(n: float) -> str:
    if int(n) != n:
        raise ValueError("n must be an integer")
    else:
        n = int(n)
    # Currently does not support integer string for n; e.g., n = "8".
    
    string = ""
    for i in range(1, n+1):
        string += str(i)
    return string
#print(one_to_n(8))


def factorial(n: int) -> int:
    if int(n) != n:
        raise ValueError("n must be an integer")
    
    i = 1
    for j in range(2, n+1):
        i *= j
    return i
#print(factorial(5))


# https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
def colNum_to_letters(column_int: int) -> str:
    start_index = 0
    letter = ''
    
    while column_int > 25 + start_index:   
        letter += chr(65 + int((column_int-start_index)/26) - 1)
        column_int = column_int - (int((column_int-start_index)/26))*26
    letter += chr(65 - start_index + (int(column_int)))
    
    return letter
#print(colNum_to_letter(36))
