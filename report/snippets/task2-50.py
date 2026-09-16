a, b = small.copy(), other.copy()
print(np.concatenate((a, b), 1))
print(np.hstack((a, b)))
print(np.column_stack((a, b)))
print(np.c_[a, b])

