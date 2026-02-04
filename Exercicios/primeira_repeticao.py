def primeira_repeticao(array):
    vistos = []

    for number in array:
      if number in vistos:
        return number
      vistos.append(number)

    return None

print(primeira_repeticao([3, 1, 4, 1, 5]))
