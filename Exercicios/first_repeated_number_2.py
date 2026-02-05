def first_repeated_number(numbers):
  verified_numbers = set()

  for number in numbers:
    if number in verified_numbers:
      return number
    verified_numbers.add(number)

  return -1

print(first_repeated_number([0, 1, 3, 4]))