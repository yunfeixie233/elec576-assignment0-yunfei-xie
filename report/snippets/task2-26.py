a = threshold.copy()
v = np.array([0.3, 0.9, 0.7])
print(a[:, np.nonzero(v > 0.5)[0]])

