def alphabet_position(text):
  alphabet = [
      "a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z"
  ]
  result = []

  for letter in text.lower(): # Converte o texto para minúsculo para evitar problema com "A" vs "a".
    if letter in alphabet: # Garante que apenas letras serão processadas.
      position = alphabet.index(letter) + 1 # Ajusta a posição no alfabato (index começa no 0)
      result.append(str(position)) # Armazena toda as posições em string para o array de resultado, precisa ser em string para usar o join depois

  return " ".join(result) # Junta todos os números separados por espaço.