def high_and_low(numbers):
  numbers_as_string = numbers.split()
  numbers_as_integers = []

  for num_str in numbers_as_string:
    num_int = int(num_str)
    numbers_as_integers.append(num_int)

  numbers_as_integers.sort()
  highest_number = numbers_as_integers[-1]
  lowest_number = numbers_as_integers[0]

  return f"{highest_number} {lowest_number}"