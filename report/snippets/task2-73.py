a = spd.copy()
b = np.array([1., 2., 3.])
x, info = cg(a, b, rtol=1e-12, atol=0.0)
print(x)
print(info)

