def binarySearch(arr, target):
  arr.sort()
  l = 0  # Initialize `l` here
  r = len(arr) - 1

  while r >= l:
    m = (l + r) // 2
    if target == arr[m]:
      return m
    elif target < arr[m]:
      r = m - 1
    else:
      l = m + 1
  return -1


arr = [5, 9, 4, 1, 3]
target = 3

print(binarySearch(arr, target))
