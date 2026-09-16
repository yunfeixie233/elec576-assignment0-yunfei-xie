a = threshold.copy()
v = np.array([0.3, 0.9, 0.7])
print(a[:, v.T > 0.5])
v = v.reshape(-1, 1)
print(a[:, v.ravel() > 0.5])

