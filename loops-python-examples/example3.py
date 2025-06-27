numbers = [3, 6, 2, 8]

for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        print(numbers[i], end=' ')
print() 
# Esse código percorre a lista `numbers` e imprime os elementos que são menores que o próximo elemento.
# A saída será: 3 2
# Isso significa que 3 é menor que 6 e 2 é menor que 8
# O último elemento (8) não é impresso porque não há um próximo elemento para compará-lo.
# A função `print()` no final garante que a saída termine com uma nova linha
# e não fique na mesma linha do prompt de comando.
# A função `end=' '` na chamada de `print()` garante que os números sejam impressos na mesma linha, separados por um espaço.
# Se você quiser que os números sejam impressos em linhas separadas, você pode remover o `end=' '` e usar apenas `print(i)`
# ou `print(numbers[i])` dentro do loop.
# O len - 1 é usado porque queremos compara o elemento atual com o próximo, e o último elemento não tem um próximo para comparar.