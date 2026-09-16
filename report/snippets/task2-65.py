a = small.copy()
b = np.array([[1., 2.], [4., 3.]])
x = linalg.solve(a.T, b.T).T
print(x)
print(x @ a)

