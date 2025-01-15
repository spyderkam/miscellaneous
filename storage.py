#!/usr/bin/env python3

__author__ = "spyderkam"

from datetime import datetime
from multiprocessing import Process
import os


def clear(): 
  """Clear terminal."""
  os.system('clear')


# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
def f7(seq):
  seen = set()
  seen_add = seen.add
  return [x for x in seq if not (x in seen or seen_add(x))]
#print(f7([1, 2, 4, 5, 3, 5]))


def one_to_n(n: int) -> str:
  """Return a string of numbers from 1 to n."""
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
  """Return the factorial of n."""
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


def getLetters(*headers, dataFrame):
  """Get Excel column letters for given header names."""    
  letters = {}
  for header in headers:
    column_number = dataFrame.columns.get_loc(header) 
    letters[header] = colNum_to_letter(column_number)
  return letters


def getHeaders(*letters, dataFrame):
  """Get header names for given Excel column letters."""
  HEADERS = list(dataFrame.columns)
  headers = {}
  for letter in letters:
    column_number = colLetter_to_Num(letter)
    if column_number < len(HEADERS):
      headers[letter] = HEADERS[column_number]
  return headers


# https://stackoverflow.com/questions/23861680/convert-spreadsheet-number-to-column-letter
def colNum_to_letter(column_int: int) -> str:
  """Same as xlsxwriter's utility.xl_col_to_name method."""
    
  start_index = 0
  letter = ''
  
  while column_int > 25 + start_index:   
    letter += chr(65 + int((column_int-start_index)/26) - 1)
    column_int = column_int - (int((column_int-start_index)/26))*26
  letter += chr(65 - start_index + (int(column_int)))
  
  return letter
#print(colNum_to_letter(36))


def colLetter_to_Num(letter: str) -> int:
  """Convert Excel column letter to number (A=0, B=1, etc.)"""
  return sum((ord(char) - ord('A') + 1) * (26 ** i)
               for i, char in enumerate(reversed(letter))) - 1


def preZeroString(n: int, digits: int) -> str:
  """Return a string of n with pre-zeroes."""
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
  """Check if input is an integer."""
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
  """Returns a range of numbers from 1 to n."""
  return range(1, n+1)


def mmddyy():
  """Extracting the current date in MMDDYY format."""
  
  NOW = datetime.now()
  YEAR = str(NOW.year)[2:]
  MONTH = str(NOW.month)
  DAY = str(NOW.day)

  if len(MONTH) == 1:
    MONTH = "0" + MONTH
  if len(DAY) == 1:
    DAY = "0" + DAY

  return MONTH + DAY + YEAR, (MONTH, DAY, YEAR)
    
