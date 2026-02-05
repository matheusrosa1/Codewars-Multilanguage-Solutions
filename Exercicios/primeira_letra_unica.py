def primeira_letra_unica(s: str) -> int:
  freq = Counter(s)
  for index, letter in enumerate(s):
    if freq[letter] == 1:
      return index

  return 0