def first_repeated_number(numbers):
  verified_numbers = []
  for number in numbers:
    if number in verified_numbers:
      return number
    verified_numbers.append(number)
  
  return -1
