def bouncing_ball(h: float, bounce: float, window: float) -> int:
    """
    Retorna o número de vezes que a mãe verá a bola.
    Se parâmetros inválidos, retorna -1.
    """
    # Validações exigidas pelo enunciado
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    count = 0
    # Enquanto a altura atual for > window, a bola passa em queda
    while h > window:
        # queda passando pela janela
        count += 1
        # altura após o quique
        h = h * bounce
        # se após o quique a altura máxima for ainda > window, ela verá a subida
        if h > window:
            count += 1

    return count

# Exemplos
print(bouncing_ball(3, 0.66, 1.5))  # saída: 3
print(bouncing_ball(3, 1, 1.5))     # saída: -1 (rebote inválido)
