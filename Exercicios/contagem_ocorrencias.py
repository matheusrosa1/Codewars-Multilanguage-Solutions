def contagem_ocorrencias(array):
  result = {}
  for string in array:
    palavra = string.lower()

    if palavra in result:
      result[palavra] += 1
    else:
      result[palavra] = 1

  duplicados = {}

  for palavra, quantidade in result.items():
    if quantidade > 1:
      duplicados[palavra] = quantidade

  return duplicados

print(contagem_ocorrencias(["banana", "banana", "abacate", "abacate", "abacate", "uva", "uva", "uva", "uva"]))