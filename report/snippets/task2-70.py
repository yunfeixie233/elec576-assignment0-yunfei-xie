a = np.diag([2., 3., 5., 7., 11., 13.])
D, V = eigs(a, k=3, v0=np.ones(6))
print(D)
print(V)

