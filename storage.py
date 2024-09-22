#!/usr/bin/env python3.12

from multiprocessing import Process
import os

def clear(): os.system('clear')
#clear()

# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
def f7(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]
#print(f7([1, 2, 4, 5, 3, 5]))


def one_to_n(n: int) -> str:
  if type(n) is str: n = float(n)
  
  if int(n) != n:
    raise ValueError("n must be an integer")
  else:
    N = int(float(n))
  
  string = ""
  for i in range(1, N+1):
    string += str(i)
  return string
#print(one_to_n(8))


def factorial(n: int) -> int:
  if type(n) is str: n = float(n)
  
  if int(n) != n:
    raise ValueError("n must be an integer")
  else:
    N = int(float(n))
  
  i = 1
  for j in range(2, N+1):
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


def preZeroString(n: int, digits: int) -> str:
  if type(n) is str: n = float(n)
  
  if int(n) != n:
    raise ValueError("n must be an integer")
  else:
    N = int(float(n))     # Includes "2.0". Doesn't have to be in if/else.

  if len(str(N)) < digits:
    return "0" * (digits - len(str(N))) + str(N)
  elif len(str(N)) > digits:
    raise ValueError(f"{N} must have less than {digits} digits")
  else:
    return str(N)
#print(preZeroString(2.0, 5))


def isint(n: object) -> bool:
  if type(n) is str: n = float(n)
  
  if int(n) != n:
    return False
  else:
    return True  
#print(isint(2.0), isint("2."))


# https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel
def runInParallel(*fns, daemonic=False):
  mainRunningFunctions = []
  for fn in fns:
    p = Process(target=fn)
    if fn is fns[0] and daemonic is True:
      p.daemon = True     # First process stops once others end.
      p.start()
    else:
      p.start()
      mainRunningFunctions.append(p)
  for p in mainRunningFunctions:
    p.join()
#runInParallel(func1, func2, func3)

def range1(n):
  return range(1, n+1)