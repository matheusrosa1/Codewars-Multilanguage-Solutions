def find_unique(arr):
  # Olha apenas para os três primeiros elementos
  a, b, c = arr[0], arr[1], arr[2]

  # Determina qual é o número que se repete
  if a == b:
    common = a
  elif a == c:
    return b # b é o unico
  else:
    return a # a é o unico
  
  for number in arr:
    if number != common:
      return number