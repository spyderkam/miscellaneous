#!/usr/bin/env python3

__author__ = "spyderkam"

from datetime import datetime
from multiprocessing import Process
import numpy as np
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


def arrays_almost_equal(arr1, arr2, tolerance=0.01):
  """Check if two NumPy arrays are almost equal."""

  # Ensure arrays have the same shape
  if arr1.shape != arr2.shape:
      return False

  # Convert inputs to numpy arrays
  arr1 = np.array(arr1)
  arr2 = np.array(arr2)

  # Handle zero values to avoid division by zero
  # For b == 0, check if |a| <= tolerance
  mask_zero = arr2 == 0
  zero_check = np.abs(arr1[mask_zero]) <= tolerance

  # For non-zero values, check if |a - b| <= tolerance*|b|
  mask_nonzero = ~mask_zero
  relative_check = np.abs(arr1[mask_nonzero] – arr2[mask_nonzero]) <= tolerance*np.abs(arr2[mask_nonzero])

  # Combine results: all zero cases and non-zero cases must pass
  return np.all(zero_check) and np.all(relative_check)


def arrays_within_delta(arr1, arr2, delta=1.0):
  """
  Check if corresponding elements of two NumPy arrays are within ±delta of each other.
    
  Parameters:
  arr1 : array-like
    First input array.
  arr2 : array-like
    Second input array.
  delta : float, optional
    Tolerance for equivalence (default is 1.0). Elements are equivalent if |arr1[i] - arr2[i]| <= delta.
    
  Returns:
  bool
    True if all corresponding elements are within ±delta, False otherwise.
  """
  # Convert inputs to NumPy arrays
  arr1 = np.array(arr1)
  arr2 = np.array(arr2)
    
  # Check if shapes match
  if arr1.shape != arr2.shape:
    return False
    
  # Check if absolute differences are <= delta
  return np.all(np.abs(arr1 - arr2) <= delta)
