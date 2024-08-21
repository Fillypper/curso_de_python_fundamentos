conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # se tem intersecção, caso 1 valor apareça nos dois conjuntos passados, retorna false
print(conjunto_a.isdisjoint(conjunto_c))