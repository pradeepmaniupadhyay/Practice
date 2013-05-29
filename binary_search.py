"""Program for binary search."""

__author__ = ('Pradeep Mani Upadhyay', 'pradeepmani.upadhyay@gmail.com')

def BinarySearch(arr, item, debug=False):
  """Function for binary search.

  Args:
    arr: Array to search the item.
    item: Item to be searched.
    debug: If True print debug information.

  Returns:
    True if item found in array or False.
  """
  start, end = 0, len(arr)  
  while start < end:
    if debug: print start, end
    mid = start + (end - start) / 2
    if arr[mid] < item:
      start = mid + 1
    elif arr[mid] > item:
      end = mid
    else:
      return True
  return False

if __name__ == '__main__':
  arr = range(1, 101)
  for i in range(98, 105):
    if BinarySearch(arr, i, debug=True):
      print i, 'Found'
    else:
      print i, 'Not Found'
