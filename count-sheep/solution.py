def count_sheep(n):
  murmur = ""
  for number in range(1, n + 1):
    murmur += f"{number} sheep..."
  return murmur