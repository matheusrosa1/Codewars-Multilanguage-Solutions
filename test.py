import sys

# Tamanho de um inteiro em Python
print(f"Tamanho de um inteiro: {sys.getsizeof(0)} bytes")

# Vamos tentar criar uma lista grande
try:
    big_list = [0] * 10**9  # 100 milhões de inteiros
    print(f"Lista criada com {len(big_list)} elementos")
except MemoryError:
    print("Faltou RAM!")
