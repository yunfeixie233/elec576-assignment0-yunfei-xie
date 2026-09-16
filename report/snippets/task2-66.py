a = rect.copy()
U, S, Vh = linalg.svd(a)
V = Vh.T
print(U)
print(S)
print(V)

