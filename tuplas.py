pares = [(3, 7), (1, 9), (5, 2), (10, 10)]
x = 2
y = 5
resultado = [p for p in pares if p[0] > x and p[1] > y]
print(resultado)