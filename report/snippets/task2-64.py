a = spd.copy()
b = np.array([1., 2., 3.])
print(linalg.solve(a, b))
a = rect.copy()
b = np.array([1., 2., 2.])
print(linalg.lstsq(a, b))

