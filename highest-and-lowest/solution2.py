def high_and_low(numbers):
  nums = map(int, numbers.split())

  return f"{max(nums)} {min(nums)}"