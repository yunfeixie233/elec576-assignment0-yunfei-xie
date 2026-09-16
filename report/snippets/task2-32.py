x = small.copy()
y = x[1, :].copy()
y[0] = 99
print(y)
print(x)

