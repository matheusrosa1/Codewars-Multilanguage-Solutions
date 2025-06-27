def count_consecutive_pairs(arr):
    count = 0
    
    # 1. Usamos um laço 'for' com 'range' e um passo de 2 para agrupar os pares corretamente.
    #    Isso resolve o problema da iteração e da lógica de pareamento.
    # range(start, stop, step) permite iterar sobre os índices dos pares.
    # step é 2 para pegar pares de elementos.
    # start é 0, stop é len(arr) - 1 para evitar o último elemento se for ímpar.
    # Isso garante que não acessemos um índice fora do intervalo.
    # Exemplo: se arr = [1, 2, 3, 4], os índices serão 0, 2.
    # Se arr = [1, 2, 3], os índices serão 0, 2 (o último elemento não é par).
    # Se arr = [1], não entramos no loop, pois não há pares
    for i in range(0, len(arr) - 1, 2):
        
        # 2. Acessamos os dois elementos do par diretamente usando o índice 'i'.
        num1 = arr[i]
        num2 = arr[i+1]

        # 3. Usamos abs() para verificar se são consecutivos, independentemente da ordem.
        if abs(num1 - num2) == 1:
            
            # 4. Incrementamos o contador da forma correta.
            count += 1
            
    return count