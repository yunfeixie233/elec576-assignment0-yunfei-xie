a, b = small.copy(), other.copy()
print(np.concatenate((a, b)))
print(np.vstack((a, b)))
print(np.r_[a, b])

