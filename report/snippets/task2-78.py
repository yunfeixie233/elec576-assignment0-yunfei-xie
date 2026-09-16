a = np.array([[3., 1.], [1., 4.], [2., 0.]])
I = np.argsort(a[:, 0])
b = a[I, :]
print(I)
print(b)

