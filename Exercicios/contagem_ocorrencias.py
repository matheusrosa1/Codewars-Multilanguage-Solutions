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
        duplicados[palavras] = quantidade

    return duplicados 