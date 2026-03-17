def comp(array1, array2):
  if array1 is None or array2 is None:
    return False
  
  if len(array1) != len(array2):
    return False

  array1_squared = []

  for x in array1:
    array1_squared.append(x * x)
  
  array1_squared.sort()
  array2.sort()

  return array1_squared == array2