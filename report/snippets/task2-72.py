a = small.copy()
P, L, U = linalg.lu(a)
print(P)
print(L)
print(U)
print(P @ L @ U)

