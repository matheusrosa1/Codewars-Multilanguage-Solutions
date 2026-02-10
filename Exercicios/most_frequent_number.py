def most_frequent_number(numbers):
  counter = {}
  most_frequent = numbers[0]
  max_count = 0

  for number in numbers:
    if number in counter:
      counter[number] += 1
    else:
      counter[number] = 1
    
    if counter[number] > max_count:
      max_count = counter[number]
      most_frequent = number
  
  return most_frequent