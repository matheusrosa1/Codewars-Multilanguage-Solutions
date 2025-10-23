def rental_car_cost(d):
    cost = 40 * d
    
    # Primeiro, checa a condição de maior desconto (7 ou mais dias)
    if d >= 7:
        cost -= 50
    # Se a primeira falhou, checa a segunda condição (3 ou mais dias)
    # A regra é "3 ou mais", por isso 'd >= 3'
    elif d >= 3:
        cost -= 20
    
    # Se nenhuma das condições (d >= 7 ou d >= 3) for verdadeira,
    # nenhum desconto é aplicado e o custo original é retornado.
    return cost