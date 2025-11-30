def is_uppercase(inp):
  for char in inp:
    if char.isalpha() and char.islower():
      return False
  return True