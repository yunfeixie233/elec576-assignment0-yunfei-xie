a = spd.copy()
b = np.diag([1., 2., 3.])
D, V = linalg.eig(a, b)
print(D)
print(V)

