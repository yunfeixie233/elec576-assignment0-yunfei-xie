Z = rect.copy()
y = np.array([1., 2., 2.])
x = linalg.lstsq(Z, y)
print(x)
print(Z @ x[0])

