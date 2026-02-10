def is_valid_walk(walk):
    # Regra 1:
    # A caminhada precisa ter exatamente 10 passos,
    # pois cada passo representa 1 minuto
    if len(walk) != 10:
        return False

    # Contamos quantas vezes cada direção aparece no array
    n_direction = walk.count('n')
    s_direction = walk.count('s')
    e_direction = walk.count('e')
    w_direction = walk.count('w')

    # Regra 2:
    # Para voltar ao ponto inicial:
    # - o número de passos para o norte deve ser igual ao sul
    # - o número de passos para o leste deve ser igual ao oeste
    if n_direction == s_direction and e_direction == w_direction:
        return True

    # Caso qualquer uma das condições acima falhe,
    # a caminhada não é válida
    return False
