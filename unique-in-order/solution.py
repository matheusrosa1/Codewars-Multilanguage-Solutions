def unique_in_order(sequence):
  # Criamos uma lista vazia que armazenará o resultado final
  result = []

  # Percorremos cada elemento da sequencia recebida (pode ser string, lista ou tupla)
  for item in sequence:
    # Verificamos duas situações:
    # 1. Se 'result' ainda está vazio (não temos nenhum elemento adicionado)
    # 2. OU se o item atual é diferente do ultimo elemento já adicionado em 'result'
    # Isso garante que resolvemos apenas duplicados consecutivos
    if not result or item != result[-1]:
      result.append(item)
    
    return result