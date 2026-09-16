a, b = small.copy(), other.copy()
c, d = np.eye(2), np.zeros((2, 2))
print(np.block([[a, b], [c, d]]))

